const Order = require("../models").Order;
const { Op } = require("sequelize");
const { ocClient, storeClient } = require('../services/mainServer');
const products = require("../utils/productos.json");
const Axios = require("axios");
const { depachar } = require('../services/dataBase');
const { generateHash } = require("../utils/cryptoHelpers");
const { get_sku_stock_almacen, move_product_to_almacen } = require('./utils.controller');
const colors = require('colors');


async function get(req, res) {
    try {

        var pending_ftp = await Order.findAll({
            where: {
                state: 'en_proceso',
                canal: 'ftp'
            }
        });

        var accepted_ftp = await Order.findAll({
            where: {
                state: 'aceptada',
                canal: 'ftp'
            }
        });

        var completed_ftp = await Order.findAll({
            where: {
                state: 'finalizada',
                canal: 'ftp'
            }
        });

        var pending_group = await Order.findAll({
            where: {
                state: 'en_proceso',
                canal: {
                    [Op.or]: ['b2b', 'b2c']
                }
            }
        });

        var accepted_group = await Order.findAll({
            where: {
                state: 'aceptada',
                canal: {
                    [Op.or]: ['b2b', 'b2c']
                }
            }
        });

        var completed_group = await Order.findAll({
            where: {
                state: 'finalizada',
                canal: {
                    [Op.or]: ['b2b', 'b2c']
                }
            }
        });

        const count_pending_ftp = await Order.count({ where: { state: 'en_proceso', canal: 'ftp' } });
        const count_accepted_ftp = await Order.count({ where: { state: 'aceptada', canal: 'ftp' } });
        const count_completed_ftp = await Order.count({ where: { state: 'finalizada', canal: 'ftp' } });

        const count_pending_group = await Order.count({
            where: {
                state: 'en_proceso',
                canal: {
                    [Op.or]: ['b2b', 'b2c']
                }
            }
        });
        const count_accepted_group = await Order.count({
            where: {
                state: 'aceptada',
                canal: {
                    [Op.or]: ['b2b', 'b2c']
                }
            }
        });
        const count_completed_group = await Order.count({
            where: {
                state: 'finalizada',
                canal: {
                    [Op.or]: ['b2b', 'b2c']
                }
            }
        });

        return res.status(200).render('Oc', {
            count_pending_ftp: count_pending_ftp,
            count_accepted_ftp: count_accepted_ftp,
            count_completed_ftp: count_completed_ftp,
            pending_ftp: pending_ftp,
            accepted_ftp: accepted_ftp,
            completed_ftp: completed_ftp,
            count_pending_group: count_pending_group,
            count_accepted_group: count_accepted_group,
            count_completed_group: count_completed_group,
            pending_group: pending_group,
            accepted_group: accepted_group,
            completed_group: completed_group
        });

    } catch (error) {
        console.log(error.message);
        return res.status(500).send(error.message);
    }

}

async function post(req, res) {
    console.log(`Hemos recibido una orden b2b de otro grupo`.green);
    return res.status(400).send("No se reciben b2b");
    // try {
    //     const ocId = req.params['id'];

    //     const ocData = await ocClient.get(`/obtener/${ocId}`, {
    //         headers: {
    //             'Content-Type': 'application/json'
    //         }
    //     });

    //     const order = ocData.data[0];

    //     const cliente = order.cliente;
    //     const sku = order.sku;
    //     const fechaEntrega = order.fechaEntrega;
    //     const cantidad = order.cantidad;
    //     const urlNotificacion = order.urlNotificacion;
    //     console.log(`Hemos recibido una orden b2b de otro grupo`.green);
    //     if (!(products[sku]["group"].includes(13))) {
    //         console.log(`El producto ${sku} no pertenece al grupo 13 por lo que la rechazamos`.red);
    //         await ocClient.post(`/rechazar/${ocId}`, {
    //             "rechazo": "Rechazada por falta de stock"
    //         }, {
    //             headers: {
    //                 'Content-Type': 'application/json'
    //             }
    //         });
    //         await Axios.patch(urlNotificacion, {
    //             "estado": "rechazada"
    //         }, {
    //             headers: {
    //                 'Content-Type': 'application/json'
    //             }
    //         });
    //     } else {
    //         console.log(`El producto ${sku} pertenece al grupo 13 por lo que revisamos nuestro stock`.green);
    //         let authHash = generateHash('GET');
    //         var stores = await storeClient.get('/almacenes', {
    //             headers: {
    //                 'Authorization': `${process.env.BASE_AUTH_TOKEN}${authHash}`
    //             }
    //         });
    //         stores = stores.data;
    //         console.log(`Stores obtenidas correctamente`.green);
    //         stock = await Axios.get(`http://localhost:${process.env.PORT}/stocks`);
    //         console.log(`Stock obtenido correctamente desde localhost`.green);
    //         stockObject = {}
    //         for (const item of stock.data) {
    //             stockObject[item.sku] = item.stock;
    //         }

    //         let availableStock = stockObject[sku];

    //         if (!availableStock) {
    //             availableStock = 0;
    //         }

    //         console.log(`El stock disponible del producto ${sku} es ${availableStock}`.blue);

    //         if (availableStock - cantidad >= 20) {
    //             console.log(`El stock disponible del producto ${sku} es suficiente para la orden, intentamo aceptar`.green);
    //             const ocAceptada = await ocClient.post(`/recepcionar/${ocId}`, {}, {
    //                 headers: {
    //                     'Content-Type': 'application/json'
    //                 }
    //             });
    //             if (ocAceptada.status === 200) {
    //                 console.log(`La orden ${ocId} ha sido aceptada correctamente en el servidor`.green);
    //             } else {
    //                 console.log(`La orden ${ocId} no ha podido ser aceptada en el servidor`.red);
    //             }
    //             newOrder = await Order.create({
    //                 internalid: ocId,
    //                 cliente: cliente,
    //                 fechaentrega: fechaEntrega,
    //                 sku: sku,
    //                 cantidad: cantidad,
    //                 urlnotificacion: urlNotificacion,
    //                 state: 'aceptada',
    //                 canal: 'b2b',
    //             });
    //             console.log(`La orden ${ocId} ha sido creada en la base de datos`.green);
    //             const despacho = stores.filter(store => store.despacho)[0];
    //             const not_despacho = stores.filter(store => !store.despacho);
    //             var missing = cantidad;

    //             for (almacen of not_despacho) {
    //                 if (missing === 0) {
    //                     console.log(`La orden ${ocId} ha sido completada correctamente, enviados ${cantidad} ${sku}`.rainbow);
    //                     stockObject[order.sku] -= order.cantidad;
    //                     await Order.update({ state: 'finalizada' }, { where: { internalid: ocId } });
    //                     console.log(`La orden ${ocId} ha sido actualizada en nuestra DB`.green);
    //                     break;
    //                 }
    //                 let product = await get_sku_stock_almacen(order.sku, almacen._id);
    //                 // product = [{sku: 'sku', _id: 'id'}, {sku: 'sku', _id: 'id'}]
    //                 if (product.length) {
    //                     console.log(`El producto ${sku} tiene stock en el almacen ${almacen._id}`.green);
    //                     for (let producto of product) {
    //                         missing--;
    //                         console.log(`Intentando mover producto desde almacen ${almacen._id}`.blue);
    //                         await move_product_to_almacen(producto._id, "despacho");
    //                         console.log(`Comenzando despacho`.blue);
    //                         await depachar(order, producto);
    //                         if (missing === 0) {
    //                             break;
    //                         }
    //                     }
    //                 }
    //                 if (missing === 0) {
    //                     console.log(`La orden ${ocId} ha sido completada correctamente, enviados ${cantidad} ${sku}`.rainbow);
    //                     stockObject[order.sku] -= order.cantidad;
    //                     await Order.update({ state: 'finalizada' }, { where: { internalid: ocId } });
    //                     console.log(`La orden ${ocId} ha sido actualizada en nuestra DB`.green);
    //                     break;
    //                 }
    //             }
    //         } else {
    //             // Rechazar
    //             console.log(`El producto ${sku} esta bajo en stock por lo que rechazamos`.red);
    //             await ocClient.post(`/rechazar/${ocId}`, {
    //                 "rechazo": "Rechazada por falta de stock"
    //             }, {
    //                 headers: {
    //                     'Content-Type': 'application/json'
    //                 }
    //             });
    //             console.log(`La orden ${ocId} ha sido rechazada en el servidor`.green);
    //             await Axios.patch(urlNotificacion, {
    //                 "estado": "rechazada"
    //             }, {
    //                 headers: {
    //                     'Content-Type': 'application/json'
    //                 }
    //             });

    //             return res.status(400).send({
    //                 estado: 'rechazada'
    //             });
    //         }
    //     }
    //     return res.status(201).send({
    //         id: ocId,
    //         estado: 'recibida',
    //         ...order
    //     });

    // } catch (error) {
    //     console.log(error.message);
    //     return res.status(500).send(error.message);
    // }

};

async function patch(req, res) {
    try {
        console.log("update received", data);
        const order = await Order.findOne({
            where: {
                internalid: req.params['id'],
            }
        });
        if (!order) {
            res.status(404).send({ message: 'No se encontro el pedido' });
        }
        await order.update({
            estado: data.estado
        });
        return res.status(204).send();

    } catch (error) {
        console.log(error.message);
        return res.status(500).send(error.message);
    }

};

module.exports = {
    get,
    post,
    patch,
};