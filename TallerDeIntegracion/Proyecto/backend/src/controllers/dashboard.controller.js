const { storeClient, factoryClient } = require('../services/mainServer');
const { generateHash } = require('../utils/cryptoHelpers');
const products = require("../utils/productos.json");

async function get(req, res) {
    try {
        let authHash;
        authHash = generateHash('GET');
        const stores = await storeClient.get('/almacenes', {
            headers: {
                'Authorization': `${process.env.BASE_AUTH_TOKEN}${authHash}`
            }
        });

        var usage_level = {};
        const stock_recepcion = {};
        const stock_cocina = {};
        const stock_despacho = {};
        const stock_pulmon = {};
        const stock_general = {};
        const individual = {};
        const stock_drinks = {};
        const stock_dishes = {};
        const stock_trays = {};

        const ingredients = {};
        Object.keys(products).map(function(key) {
            ingredients[key] = products[key]['name'];
        });

        for (const store of stores.data) {

            if (store.recepcion) {
                usage_level['recepcion'] = (store.usedSpace / store.totalSpace) * 100;
            } else if (store.cocina) {
                usage_level['cocina'] = (store.usedSpace / store.totalSpace) * 100;
            } else if (store.despacho) {
                usage_level['despacho'] = (store.usedSpace / store.totalSpace) * 100;
            } else if (store.pulmon) {
                usage_level['pulmon'] = (store.usedSpace / store.totalSpace) * 100;

            } else {
                usage_level['general'] = (store.usedSpace / store.totalSpace) * 100;
            }

            authHash = generateHash(`GET${store._id}`);
            const availableSKUSResponse = await storeClient.get('/skusWithStock', {
                params: {
                    almacenId: store._id,
                },
                headers: {
                    'Authorization': `${process.env.BASE_AUTH_TOKEN}${authHash}`,
                }
            })
            const availableItems = availableSKUSResponse.data;

            for (const item of availableItems) {
                if (store.recepcion) {
                    stock_recepcion[item._id] = item.total;
                } else if (store.cocina) {
                    stock_cocina[item._id] = item.total;
                } else if (store.despacho) {
                    stock_despacho[item._id] = item.total;
                } else if (store.pulmon) {
                    stock_pulmon[item._id] = item.total;
                } else {
                    stock_general[item._id] = item.total;
                }

                if (item._id < 1000) {
                    if (!individual[item._id]) {
                        individual[item._id] = item.total;
                    } else {
                        individual[item._id] += item.total;
                    }
                } else if (item._id < 2000) {
                    if (!stock_drinks[item._id]) {
                        stock_drinks[item._id] = item.total;
                    } else {
                        stock_drinks[item._id] += item.total;
                    }
                } else if (item._id < 10000) {
                    if (!stock_dishes[item._id]) {
                        stock_dishes[item._id] = item.total;
                    } else {
                        stock_dishes[item._id] += item.total;
                    }
                } else {
                    if (!stock_trays[item._id]) {
                        stock_trays[item._id] = item.total;
                    } else {
                        stock_trays[item._id] += item.total;
                    }
                }
            }
        }

        return res.status(200).render('Dashboard', {
            usage_level: usage_level,
            stock_recepcion: stock_recepcion,
            stock_cocina: stock_cocina,
            stock_despacho: stock_despacho,
            stock_pulmon: stock_pulmon,
            stock_general: stock_general,
            ingredients: ingredients,
            individual: individual,
            drinks: stock_drinks,
            dishes: stock_dishes,
            trays: stock_trays
        });

    } catch (error) {
        console.log(error);
        return res.status(500).send(error);
    }

}

module.exports = {
    get,
};