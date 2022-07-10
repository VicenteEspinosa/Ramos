const { generateHash } = require("../utils/cryptoHelpers");
const { get_stock } = require("./stock.controller");
const products = require("../utils/productos.json");
const {
    amount_in_cocina,
    find_product_out_cocina,
    move_product_to_almacen,
    sleep,
    get_sku_stock_almacen
} = require('./utils.controller');
const { createOrder } = require('./ocCreate.controller')
const lodash = require("lodash");
const colors = require("colors");

const { factoryClient, storeClient } = require("../services/mainServer");

const MAX_PER_REQUEST = 20;
const EXPECTED_STOCK = 40;

async function moveItem(storage, productoId) {
    console.log(`Moviendo ${productoId} a ${storage}`.blue);
    try {
        let authHash;
        authHash = generateHash("GET");
        const stores = await storeClient.get("/almacenes", {
            headers: {
                Authorization: `${process.env.BASE_AUTH_TOKEN}${authHash}`,
            },
        });

        const storageIds = {};

        for (const store of stores.data) {
            if (store.recepcion) storageIds["recepcion"] = store._id;
            if (store.despacho) storageIds["despacho"] = store._id;
            if (store.pulmon) storageIds["pulmon"] = store._id;
            if (store.cocina) storageIds["cocina"] = store._id;
            if (!store.recepcion && !store.despacho && !store.pulmon && !store.cocina)
                storageIds["general"] = store._id;
        }

        authHash = generateHash(`POST${productoId}${storageIds[storage]}`);
        const storeResponse = await storeClient.post(
            "moveStock", { productoId: productoId, almacenId: storageIds[storage] }, {
                headers: {
                    Authorization: `${process.env.BASE_AUTH_TOKEN}${authHash}`,
                    "Content-Type": "application/json",
                },
            }
        );
        console.log(" Move Item response -----------");
        if (storeResponse.status === 200) {
            console.log(`Se ha movido ${productoId} a ${storage} exitosamente`.green);
        }
        await sleep(34);
        return storeResponse.data;
    } catch (error) {
        console.log(`Ha ocurrido un error al mover ${productoId} a ${storage}`.red);
        console.log(error.message);
        if (error.code === 'ECONNABORTED') {
            console.log("Problemas en el servidor del curso... Retrying in 3 seconds...".yellow);
            await sleep(3000);
            return await moveItem(storage, productoId)
        }
        return null;
    }
}

async function requestItem(sku, cantidad) {
    try {
        console.log("REQUEST ITEM -----------".blue);
        console.log(`Se intentará fabricar ${cantidad} de ${sku}`.blue);
        let authHash;
        authHash = generateHash(`PUT${sku}${cantidad}`);
        const factoryResponse = await factoryClient.put(
            "/fabricarSinPago", { sku: sku, cantidad: cantidad }, {
                headers: {
                    Authorization: `${process.env.BASE_AUTH_TOKEN}${authHash}`,
                    "Content-Type": "application/json",
                },
            }
        );
        if (factoryResponse.status === 200) {
            console.log(`Se ha fabricado ${cantidad} de ${sku} exitosamente`.green);
        }
        return factoryResponse.data;
    } catch (error) {
        console.log(`Ha ocurrido un error al fabricar ${cantidad} de ${sku}`.red);
        console.log(error.message);
        if (error.code === 'ECONNABORTED') {
            console.log("Retrying in 3 seconds...");
            await sleep(3000);
            return await requestItem(sku, cantidad)
        }
        return null;
    }
}

async function missingStock(stock) {
    console.log("Revisando Stock Faltante...".blue);
    var missing = {};
    const skus = Object.keys(products);
    for (const sku of skus) {
        if (stock[sku]) {
            if (stock[sku] < EXPECTED_STOCK) {
                missing[sku] =
                    EXPECTED_STOCK - stock[sku] > MAX_PER_REQUEST ?
                    MAX_PER_REQUEST :
                    EXPECTED_STOCK - stock[sku];
            }
        } else {
            missing[sku] = MAX_PER_REQUEST;
        }
    }
    return missing;
}

async function restock_base() {
    console.log("Restocking...".blue);
    const stock = await get_stock();
    console.log("Nuestro stock actual".blue);
    console.log(stock);
    const missing = await missingStock(stock);
    console.log("Nuestro stock faltante".blue);
    console.log(missing);
    const sortedSkus = Object.keys(missing).sort(function(a, b) {
        return missing[b] - missing[a];
    });
    if (sortedSkus.includes('10000') && sortedSkus.includes('12000')) { // Comparten platos
        if (missing['10000'] > missing['12000']) {
            console.log("Faltan más platos de 10000 que de 12000".blue);
            // Cambiar orden de 12000 y 10000, para hacer primero 10000
            let index12000 = sortedSkus.indexOf('12000');
            sortedSkus[sortedSkus.indexOf('10000')] = '12000';
            sortedSkus[index12000] = '10000';
        }
    }

    for (const sku of sortedSkus) {
        let max_batches_producible = parseInt(MAX_PER_REQUEST / products[sku].batch_size);
        console.log(
            `Faltan ${missing[sku]} (${closestNumber(
        missing[sku],
        products[sku].batch_size
      )}) ${products[sku].name}`.yellow
        );

        products[sku]["requires"].map((requirement) => {
            if (stock[requirement[0]] < requirement[1] * missing[sku]) {
                let max_batches = parseInt(stock[requirement[0]] / requirement[1]);
                if (max_batches < max_batches_producible) {
                    max_batches_producible = max_batches;
                }
            } else if (!stock[requirement[0]]) {
                max_batches_producible = 0;
                console.log(`Nos falta ${products[requirement[0]].name} para producirlo`.red);
            } else {
                missing[requirement[0]] = missing[requirement[0]] + requirement[1] * missing[sku];
            }
        });
        if (max_batches_producible > 0) {
            console.log(`Se requieren ${max_batches_producible} batches de ${products[sku].name}`.yellow);
            for (let i = 0; i < max_batches_producible; i++) {
                console.log(`Se requiere ${products[sku].name} y nosotros lo producimos`.blue);
                for (const requerimentArray of products[sku]["requires"]) {
                    const requeriment = requerimentArray[0];
                    let amount = requerimentArray[1] * products[sku].batch_size;
                    // Mover cosas
                    stock[requeriment] -= amount;
                    amount -= await amount_in_cocina(requeriment);
                    console.log(`Hay que mover ${amount} de ${products[requeriment].name}`);
                    for (let e = 0; e < amount; e++) {
                        const product = await find_product_out_cocina(requeriment);
                        if (product) {
                            await moveItem('cocina', product["_id"])
                        } else {
                            console.log("No hay elementos para mover");
                        }
                    }
                }
                await requestItem(sku, products[sku].batch_size)
            }
        } else {
            delete missing[sku];
            console.log(`No se puede fabricar ${products[sku].name}`.blue);
        }
    }
    console.log("Comienza la limpieza de la cocina".blue);
    try {
        let authHash = generateHash('GET');
        var stores = await storeClient.get('/almacenes', {
            headers: {
                'Authorization': `${process.env.BASE_AUTH_TOKEN}${authHash}`
            }
        });
        let cocina = stores.data.filter(store => store.cocina)[0];
        const stockObject = await get_stock();
        for (let sku of Object.keys(stockObject)) {
            let productsInCocina = await get_sku_stock_almacen(sku, cocina._id);
            for (let product of productsInCocina) {
                await move_product_to_almacen(product._id, "general");
            }
        }
        console.log("Se limpió la cocina correctamente".green);
    } catch (e) {
        console.log("Fallo limpiar la cocina".red);
        console.log(e.message);
    }
    console.log("Ha finalizado el restock de elementos".green);
    return missing;
}

async function restock(req, res) {
    var missing = await restock_base();
    res.status(200).send(missing);
}

function closestNumber(amount, batch_size) {
    let quotient = parseInt(amount / batch_size);
    let n1 = batch_size * quotient;
    let n2 =
        amount * batch_size > 0 ?
        batch_size * (quotient + 1) :
        batch_size * (quotient - 1);
    if (Math.abs(amount - n1) < Math.abs(amount - n2)) return n1;
    return n2;
}

module.exports = {
    restock,
    restock_base,
    closestNumber,
};