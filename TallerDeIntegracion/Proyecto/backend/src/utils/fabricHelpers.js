const { factoryClient, storeClient } = require('../services/mainServer')
const { generateHash } = require("../utils/cryptoHelpers");
const { moveItem } = require('../controllers/fabricateSku.controller')
    /* const { sleep } = require('../controllers/fabricateSku.controller'); */

async function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
        currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}

async function requestItem(sku, cantidad) {
    try {
        console.log("REQUEST ITEM -----------");
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
        console.log(" Request Item response -----------");
        console.log(factoryResponse.data);
        return factoryResponse.data;
    } catch (error) {
        console.log("REQUEST ITEM ERROR -----------");
        console.log(error);
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
        console.log("GET SKU STOCK AMACEN -----------");
        console.log(almacenId);
        console.log(`Getting ${sku} from ${almacenId}`);
        authHash = generateHash(`GET${almacenId}${sku}`);
        const skuStockResponse = await storeClient.get("/stock", {
            params: {
                almacenId: almacenId,
                sku: sku,
            },
            headers: {
                Authorization: `${process.env.BASE_AUTH_TOKEN}${authHash}`,
            },
        });
        return skuStockResponse.data;
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
};