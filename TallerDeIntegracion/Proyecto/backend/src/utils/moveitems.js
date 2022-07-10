const { get_sku_stock_almacen, moveItem, sleep } = require('../controllers/utils.controller');
const { generateHash } = require("./cryptoHelpers");
const { factoryClient, storeClient } = require("../services/mainServer");
const colors = require('colors');



async function get_almacenes() {
    var kitchen = {};
    var recepcion = {};
    var general = {};
    var pulmon = {};
    var despacho = {};
    let authHash = generateHash('GET');
    const almacenes = await storeClient.get('/almacenes', {
        headers: {
            'Authorization': `${process.env.BASE_AUTH_TOKEN}${authHash}`
        }
    });
    for (const almacen of almacenes.data) {
        if (almacen.cocina) {
            kitchen["_id"] = almacen["_id"];

        } else if (almacen.recepcion) {
            recepcion["name"] = "recepcion";
            recepcion["_id"] = almacen["_id"];
            recepcion["totalSpace"] = almacen["totalSpace"];
            recepcion["usedSpace"] = almacen["usedSpace"];
        } else if (almacen.pulmon) {
            pulmon["_id"] = almacen["_id"];
        } else if (almacen.despacho) {
            despacho["_id"] = almacen["_id"];
        } else {
            general["name"] = "general";
            general["_id"] = almacen["_id"];
            general["totalSpace"] = almacen["totalSpace"];
            general["usedSpace"] = almacen["usedSpace"];
        }
    }
    return [kitchen, recepcion, pulmon, general, despacho];
}

async function get_skus(almacenId) {
    try {
        authHash = generateHash(`GET${almacenId}`);
        const skuStockResponse = await storeClient.get("/skusWithStock", {
            params: {
                almacenId: almacenId,
            },
            headers: {
                Authorization: `${process.env.BASE_AUTH_TOKEN}${authHash}`,
            },
        });
        if (skuStockResponse.status == 200) {
            console.log(`${skuStockResponse.data.length} skus encontrados en almacen ${almacenId}`.green);
        }
        return skuStockResponse.data;
    } catch (err) {
        console.log(`Ha ocurrido un error al intentar obtener los skus del almacen ${almacenId}`.red);
        console.log(err.message);
    }
    
}


async function move_items() {
    try {
        var skus;
        var skus_a_pasar;
        var cantidad_dispo;
        var cant = 0;
        var counter = 121;
        //Primero revisar que hayan cosas en recepción
        const [kitchen, recepcion, pulmon, general, despacho] = await get_almacenes();

        if (recepcion['usedSpace'] > 0 && (general['totalSpace'] - general['usedSpace']) > 0) {
            //Si hay cosas en recepción, y hay espacio en general, entonces se puede mover
            console.log("Hay cosas en recepción y hay espacio en general".blue);
            skus = await get_skus(recepcion['_id']);
            cantidad_dispo = general['totalSpace'] - general['usedSpace'];

            for (const sku of skus) {
                if (cantidad_dispo - cant > 0 && counter - cant > 0) {
                    console.log(`Este es el sku en el que entre: ${sku['_id']}`.blue);
                    skus_a_pasar = await get_sku_stock_almacen(sku['_id'], recepcion['_id']);

                    for (const unidad in skus_a_pasar) {
                        console.log(`Aqui realizaremos el moviemiento de ${skus_a_pasar[unidad]['_id']}`.blue);
                        await moveItem(general['name'], skus_a_pasar[unidad]['_id']);
                        sleep(1000);
                        cant = cant + 1;
                        if (cant == counter) {
                            break;
                        }

                    }

                } else {
                    break;
                }
            }
            console.log('Identifique los que si debia pasar');

        } else {
            console.log('General se encuentra lleno, no se pueden mover los items o Recepción se encuentra vacio.');
        }

        return '';

    } catch (err) {
        console.log(err.message);

        return err.message;
    }
}

module.exports = { move_items };