const { factoryClient, storeClient } = require('../services/mainServer')
const { generateHash } = require("../utils/cryptoHelpers");
const colors = require('colors');

async function moveItem(storage, productoId) {
    try {
        console.log(`Moving ${productoId} to ${storage}`.blue);
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
        if (storeResponse.status === 200) {
            console.log(`${productoId} moved to ${storage} successfully`.green);
        }
        await sleep(34);
        return storeResponse.data;
    } catch (error) {
        console.log(`Error moving ${productoId} to ${storage}`.red);
        console.log(error.message);
        if (error.code === 'ECONNABORTED') {
            console.log("Retrying in 3 seconds...");
            await sleep(3000);
            return await moveItem(storage, productoId)
        }
        return null;
    }
}

async function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
        currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}

async function requestItem(sku, cantidad) {
    try {
        console.log(`Fabricando sin pago ${cantidad} of ${sku}`.blue);
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
            console.log(`${sku} fabricated successfully`.green);
        }
        return factoryResponse.data;
    } catch (error) {
        console.log(`Error fabricating ${sku} in requestItem function`.red);
        console.log(error.message);
        if (error.code === 'ECONNABORTED') {
            console.log("Retrying in 3 seconds...");
            await sleep(3000);
            return await requestItem(sku, cantidad)
        }
        return null;
    }
}

async function move_product_to_almacen(product_id, almacen) {
    try {
        await moveItem(almacen, product_id);
    } catch (err) {
        if (err.code === 'ECONNABORTED') {
            console.log("Retrying in 3 seconds...");
            sleep(3000);
            return await move_product_to_almacen(product_id, almacen)
        }
        return err.message;
    }
}

async function get_sku_stock_almacen(sku, almacenId) {
    try {
        console.log(`Getting stock of ${sku} in almacen ${almacenId}`.blue);
        authHash = generateHash(`GET${almacenId}${sku}`);
        const skuStockResponse = await storeClient.get("/stock", {
            params: {
                almacenId: almacenId,
                sku: sku,
            },
            headers: {
                Authorization: `${process.env.BASE_AUTH_TOKEN}${authHash}`,
                "Content-Type": "application/json",
            },
        });
        return await skuStockResponse.data;
    } catch (err) {
        console.log('LINEA 116 FABRICATE.CONTROLER');
        console.log(err.message);
        if (err.code === 'ECONNABORTED') {
            console.log("Retrying in 3 seconds...");
            sleep(3000);
            return await get_sku_stock_almacen(sku, almacenId)
        }
        console.log("GET SKU STOCK ALMACEN ERROR -----------");
        console.log(err);
        return err.message;
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function fabricate_product(sku, amount) {
    console.log("FABRICANDO ========");
    try {
        return await requestItem(sku, amount);
    } catch (err) {
        return err.message;
    }
}

async function amount_in_cocina(sku) {
    const elements = await get_sku_stock_almacen(sku, kitchen)
    return await elements.length;
}

async function find_product_out_cocina(sku) {
    for (almacen of not_kitchen) {
        let product = await get_sku_stock_almacen(sku, almacen);
        if (product.length) {
            console.log(`${sku} found in ${almacen}`.green);
            if (product.length >= 2) {
                product.sort((a, b) => {
                    return new Date(a.vencimiento) - new Date(b.vencimiento);
                });
                console.log(`El producto que esta por vencer vence: ${product[0].vencimiento}`.red);
                console.log(`El producto con mayor plazo para vencer vence: ${product[product.length - 1].vencimiento}`.green);
            }
            console.log(`El producto que retornamos esta por vencer vence: ${product[0].vencimiento}`.blue);
            return product[0];
        }
    }
    return null;
}

async function move_product_to_cocina(sku) {
    await move_product_to_almacen(sku, "cocina");
}

var kitchen;
var not_kitchen = [];

async function get_almacenes() {
    let authHash = generateHash('GET');
    const almacenes = await storeClient.get('/almacenes', {
        headers: {
            'Authorization': `${process.env.BASE_AUTH_TOKEN}${authHash}`
        }
    });
    for (const almacen of almacenes.data) {
        if (almacen.cocina) {
            kitchen = almacen["_id"];
        } else {
            not_kitchen.push(almacen["_id"]);
        }
    }
}

get_almacenes();

module.exports = {
    fabricate_product,
    amount_in_cocina,
    find_product_out_cocina,
    move_product_to_cocina,
    move_product_to_almacen,
    get_sku_stock_almacen,
    moveItem,
    sleep,
};