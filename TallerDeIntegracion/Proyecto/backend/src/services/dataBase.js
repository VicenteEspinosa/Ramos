require('dotenv').config({ path: '../../.env' });
const { storeClient } = require('../services/mainServer');
const axios = require('axios');
const { generateHash } = require('../utils/cryptoHelpers');
const groupsDatabyOc = require('../utils/groupsocProduccionByOc.json');
const groupsDatabyOcIdReception = require('../utils/groupsocProduccionByOcIdReception.json');
const groupsDataDevReception = require('../utils/groupsocDevByOcIdReception.json');
const { move_product_to_almacen, get_sku_stock_almacen } = require('../controllers/utils.controller');
const { fabricate_sku_recursive_base } = require('../controllers/fabricateSku.controller');
const { get_stock } = require('../controllers/stock.controller')
const db = require('../models');
const Order = require("../models").Order;
const { Op } = require("sequelize");
const colors = require('colors');


const produceOrders = async() => {
    console.log(`Produciendo ordenes antiguas...`.blue);
    let authHash = generateHash('GET');
    let stores;
    try {
       stores = await storeClient.get('/almacenes', {
            headers: {
                'Authorization': `${process.env.BASE_AUTH_TOKEN}${authHash}`
            }
        });
        stores = stores.data;
        console.log(`Almacenes obtenidos correctamente!`.green);
    } catch (error) {
        console.log(`Ha ocurrido un error al obtener los almacenes`.red);
        console.log(error.message);
    }
    const despacho = stores.filter(store => store.despacho)[0];
    const not_despacho = stores.filter(store => !store.despacho);

    let stock = await get_stock();
    console.log(`He obtenido nuestro stock correctamente 1`.green);
    stock = Object.keys(stock).map(key => {
        return { 'sku': key, 'stock': stock[key] }
    });
    stockObject = {}
    for (const item of stock) {
        stockObject[item.sku] = item.stock;
    }
    console.log(`He obtenido nuestro stock correctamente 2`.green);
    console.log(stockObject);
    try {
        const orders = await Order.findAll({
            where: {
                state: 'en_proceso',
                fechaentrega: {
                    [Op.gt]: db.sequelize.literal('CURRENT_TIMESTAMP')
                }
            }
        });
        console.log(`Encontré ${orders.length} ordenes en proceso !`.blue);
        for (let order of orders) {
            order = order.dataValues;
            console.log(`Procesando orden ${order.internalid}`.blue);
            // Ver si ya se puede hacer
            if (stockObject[order.sku] >= order.cantidad) {
                console.log("Tenemos stock disponible para realizar la order".green);
                const productsList = [];
                let missing = order.cantidad;
                let almacen = despacho;
                let products = await get_sku_stock_almacen(order.sku, almacen._id);
                console.log("products :" + products);
                if (products.length) {
                    console.log(`Encontré ${products.length} productos de sku ${order.sku} en despacho`.green);
                    for (let product of products) {
                        productsList.push([product, 'despacho']);
                    }
                }
                for (let almacen of not_despacho) {
                    let products = await get_sku_stock_almacen(order.sku, almacen._id);
                    if (products.length) {
                        for (const product of products) {
                            productsList.push([product, almacen]);
                        }
                    }
                }
                // Order productsList by product.vencimiento
                productsList.sort((a, b) => {
                    return new Date(a[0].vencimiento) - new Date(b[0].vencimiento);
                });
                if (productsList.length >= 2) {
                    console.log(`El producto que esta por vencer vence: ${productsList[0][0].vencimiento}`.red);
                    console.log(`El producto con mayor plazo para vencer vence: ${productsList[productsList.length - 1][0].vencimiento}`.green);
                }
                console.log(`Despachando ${missing} productos de sku ${order.sku} desde almacen ${almacen._id}`.blue);
                for (let producto of productsList) {
                    let product = producto[0];
                    let almacen = producto[1];
                    if (producto[1] != 'despacho') {
                        console.log(`Moviendo ${product.sku} de ${almacen._id} a ${despacho.nombre}`.blue);
                        await move_product_to_almacen(product._id, "despacho");
                    }
                    console.log(`Intentando depachar ${product.sku}`.blue);
                    console.log(`Este product vence en: ${product.vencimiento}`.blue);
                    console.log(`El canal de la orden es: ${order.canal}`.red);
                    console.log(`Entramos a despachar FTP`.red)
                    console.log(`Intentando despachar ${product.sku} desde despacho`.blue);
                    await depachar(order, product);
                    missing--;
                    if (missing === 0) {
                        break;
                    }
                }
                stockObject[order.sku] -= order.cantidad;
                await Order.update({ state: 'finalizada' }, { where: { internalid: order.internalid } });
            } else {
                console.log("NO SE PUEDE HACER!!!!!  Falta de stock", order.sku);
            }
        }
    } catch (error) {
        console.log(error.message);
    }

    try {
        const orders = await Order.findAll({
            where: {
                state: 'aceptada',
                canal: 'ftp',
                fechaentrega: {
                    [Op.gt]: db.sequelize.literal('CURRENT_TIMESTAMP')
                }
            }
        });
        console.log("TENEMOS ", orders.length, "ORDENES ACEPTADAS PARA REALIZAR!!!");
        for (let order of orders) {
            console.log("Encontré una orden aceptada !!! 000000000000");
            order = order.dataValues;
            console.log(order.sku);
            // Ver si se puede hacer (despachar altiro) o pasar a en_proceso y pedir lo que falta
            if (stockObject[order.sku] >= order.cantidad) {
                const productsList = [];
                console.log("TENEMOS STOCK PARA ENTREGA INMEDIATA!!!!! 9999999999");
                console.log("EL OC es: " + order._id);
                let missing = order.cantidad;
                let almacen = despacho
                let products = await get_sku_stock_almacen(order.sku, almacen._id);
                if (products.length) {
                    console.log(`Encontré ${products.length} productos de sku ${order.sku} en despacho`.green);
                    for (let product of products) {
                        productsList.push([product, 'despacho']);
                    }
                }
                for (let almacen of not_despacho) {
                    let products = await get_sku_stock_almacen(order.sku, almacen._id);
                    if (products.length) {
                        for (const product of products) {
                            productsList.push([product, almacen]);
                        }
                    }
                }
                // Order productsList by product.vencimiento
                productsList.sort((a, b) => {
                    return new Date(a[0].vencimiento) - new Date(b[0].vencimiento);
                });
                if (productsList.length >= 2) {
                    console.log(`El producto que esta por vencer vence: ${productsList[0][0].vencimiento}`.red);
                    console.log(`El producto con mayor plazo para vencer vence: ${productsList[productsList.length - 1][0].vencimiento}`.green);
                }
                console.log(`Despachando ${missing} productos de sku ${order.sku} desde almacen ${almacen._id}`.blue);
                for (let producto of productsList) {
                    let product = producto[0];
                    let almacen = producto[1];
                    if (producto[1] != 'despacho') {
                        console.log(`Moviendo ${product.sku} de ${almacen._id} a almacen`.blue);
                        await move_product_to_almacen(product._id, "despacho");
                    }
                    console.log(`Intentando depachar ${product.sku}`.blue);
                    console.log(`Este product vence en: ${product.vencimiento}`.blue);
                    console.log(`El canal de la orden es: ${order.canal}`.red);
                    console.log(`Entramos a despachar FTP`.red)
                    console.log(`Intentando despachar ${product.sku} desde despacho`.blue);
                    await depachar(order, product);
                    missing--;
                    if (missing === 0) {
                        break;
                    }
                }
                stockObject[order.sku] -= order.cantidad;
                console.log(`He finalizado correctamente la order ${order.internalid}`.rainbow);
                console.log("");
                await Order.update({ state: 'finalizada' }, { where: { internalid: order.internalid } });
            } else {
                console.log(`No tenemos stock para la entrega inmediata de ${order.sku}`.yellow);
                await fabricate_sku_recursive_base(order.sku, order.cantidad);
                console.log("Realizando update de orden a en_proceso en nuestra DB".blue);
                await Order.update({ state: 'en_proceso' }, { where: { internalid: order.internalid } });
            }

        }
    } catch (error) {
        console.log(error.message);
    }
    // Limpiar despacho
    console.log(`He terminado de procesar las ordenes, intentaré limpiar el despacho`.rainbow);
    try {
        for (let sku of Object.keys(stockObject)) {
            let productsInDespacho = await get_sku_stock_almacen(sku, despacho._id);
            for (let product of productsInDespacho) {
                await move_product_to_almacen(product._id, "general");
            }
        }
        console.log("He limpiado el despacho".rainbow);
    } catch (error) {
        console.log(`Ha ocurrido un error limpiando el despacho`.red);
        console.log(error.message);
    }

    console.log();
}

const depachar = async(order, producto) => {
    try {
        console.log("DEPACHANDO ====".yellow);
        console.log(`Order canal: ${order.canal}`.yellow);
        console.log(`Order _id: ${order._id}`.yellow);
        console.log(`Order id: ${order.internalid}, producto id: ${producto._id}`.yellow);
        let ocDespachado;

        if (order.canal === 'ftp') {
            console.log('Despachando FTP'.yellow);
            const cliente = order.cliente; // '627ed16aee1e5ec96e313f67'
            const groupId = groupsDatabyOc[cliente];
            const direccion = 'casa';

            let oc = order.internalid;

            let authHash = generateHash(`DELETE${ producto._id }${ direccion }10000${ oc }`);
            ocDespachado = await storeClient.delete('/stock', {
                headers: {
                    'Authorization': `${ process.env.BASE_AUTH_TOKEN }${authHash}`,
                    'Content-Type': 'application/json'
                },
                data: {
                    productoId: producto._id,
                    oc: oc,
                    direccion: direccion,
                    precio: 10000
                }
            });
        } else {
            console.log('Despachando B2B'.yellow);
            const receptionId = groupsDatabyOcIdReception[order.cliente];

            let authHash;
            authHash = generateHash(`POST${producto._id}${receptionId}`);
            ocDespachado = await storeClient.post('moveStockBodega', {
                productoId: producto._id,
                almacenId: receptionId,
                oc: order._id,
                precio: 10000
            }, {
                headers: {
                    'Authorization': `${process.env.BASE_AUTH_TOKEN}${authHash}`,
                    'Content-Type': 'application/json'
                }
            });

        }

        console.log(`Elemento despachado correctamente!`.green);
        return ocDespachado
    } catch (error) {
        console.log("ERROR IN DEPACHAR ======================".red)
        console.log(error);
        console.log(error.message);
    }

}

module.exports = {
    produceOrders,
    depachar,
}