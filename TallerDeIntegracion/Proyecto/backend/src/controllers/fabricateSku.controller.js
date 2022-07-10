const { generateHash } = require("../utils/cryptoHelpers");
const products = require("../utils/productos.json");
const gruposDev = require("../utils/groupsocDesarrollo.json");
const gruposProd = require("../utils/groupsocProduccion.json");
const { closestNumber } = require("./keepStock.controller.js");
const { createOrder } = require("./ocCreate.controller.js");
const {
    fabricate_product,
    amount_in_cocina,
    find_product_out_cocina,
    move_product_to_almacen,
    moveItem,
    sleep,
} = require('./utils.controller')
const colors = require('colors')

// const { factoryClient, storeClient } = require("../services/mainServer");
// const axios = require('axios');

async function fabricate_sku_recursive_base(sku, amountNeeded = 1) {
    console.log(`Comenzando fabricacion recursiva de ${sku}`.blue);
    try {
        var fabricable = true;
        const requeriments = products[sku]["requires"];
        // Si es producible por nosotros
        console.log(`El producto ${sku} es producible por nosotros`.blue);
        if (requeriments.length > 0) {
            console.log(`Se necesitan requisitos para cocinar este sku`.blue);
            // Si tiene requerimientos
            for (const requerimentArray of requeriments) {
                const requeriment = requerimentArray[0];
                var amount = requerimentArray[1];
                const amountInCocina = await amount_in_cocina(requeriment);
                if (amountInCocina >= amount) {
                    // El requirimiento esta en la cocina
                    console.log(
                        `Hay suficiente ${products[requeriment]["name"]} en la cocina`.green
                    );
                    continue;
                }
                console.log(`Necesitamos ${amount} de ${products[requeriment]["name"]} y tenemos ${amountInCocina} en la cocina`.red);
                amount -= amountInCocina; // Cuanto falta por llevar a la cocina
                let amountMissing = amount;
                for (var i = 0; i < amountMissing; i++) {
                    console.log(`No tenemos suficiente stock en cocina, buscamos en otros almacenes`.blue);
                    const product = await find_product_out_cocina(requeriment);
                    console.log(`Respuesta de product`.blue);
                    console.log(product);
                    if (product) {
                        // Si hay en otra bodega (no cocina)
                        console.log(`Se encontró un ${products[requeriment]["name"]} en otra bodega`.green);
                        console.log(`Moviendo ${products[requeriment]["name"]} a cocina, faltarian ${amount}`.blue);
                        await move_product_to_almacen(product._id, "cocina");
                        amount--;
                    } else {
                        // No hay ninguno del requerimiento
                        console.log(`No tenemos disponible ${products[requeriment]["name"]} en ningun almacen, iniciando fabricacion, faltantes ${amount}`.yellow);
                        fabricable = false;
                        await fabricate_sku_recursive_base(requeriment, closestNumber(amount, products[requeriment]["batch_size"]));
                        break;
                    }
                }
            }
            if (fabricable) {
                // Habian de todos los requerimientos en alguna bodega
                console.log(`Tenemos todos los requisitos, cocinando ${products[sku]["name"]}`.green);
                await fabricate_product(sku, closestNumber(amountNeeded, products[sku]["batch_size"]));
                console.log(`${products[sku]["name"]} se ha intentado fabricar`.green);
                return 1;
            } else {
                // Falto algun ingrediente (y se mandaron a fabricar)
                console.log(
                    `Faltan ingredientes para fabricar ${products[sku]["name"]} a la fabrica`.yellow
                );
                return 0;
            }
        } else {
            // No tiene requerimientos (ingrediente)
            console.log(`El producto ${sku} no tiene requerimientos, iniciando fabricacion`.blue);
            await fabricate_product(
                sku,
                closestNumber(amountNeeded, products[sku]["batch_size"])
            );
            return 1;
        }
        // } else {
        //     // No es producible por nosotros
        //     console.log(`El producto ${products[sku]["name"]} ${sku} no es producible por nosotros`.blue);
        //     const grupos = process.env.PRODUCTION ? gruposProd : gruposDev;
        //     for (const grupo of products[sku]["group"]) {
        //         console.log(`Revisando grupo ${grupo}`.blue);
        //         if (!grupos[grupo].url) continue;
        //         try {
        //             const stock = await axios.get(`${grupos[grupo].url}/stocks`,
        //             { timeout: 2000})
        //             for (skuStock of stock.data) {
        //                 if (String(skuStock.sku) === String(sku)) {
        //                     stock_key = Object.keys(skuStock).filter(function(key) {
        //                         return key !== 'sku';
        //                     })[0]
        //                     if (parseInt(skuStock[stock_key]) >= parseInt(closestNumber(amountNeeded, products[sku]["batch_size"]))) {
        //                         try {
        //                             console.log(`Enviando OC a grupo ${grupo}`);
        //                             await createOrder(sku, closestNumber(amountNeeded, products[sku]["batch_size"]), grupo)
        //                             return 2;
        //                         } catch (err) {
        //                             console.log("Error de otro grupo: " + err.message);
        //                         }
        //                     }
        //                 }
        //             }
        //         } catch (err) {
        //             console.log(err.message);
        //             console.log(`Error al obtener stock de grupo ${grupo} en url ${grupos[grupo].url}`.america);
        //         }
        //     }
        //     return 2;
        // }
    } catch (err) {
        console.log(`Error al hacer fabricate recursive base en sku ${sku}`.red);
        console.log(err.message);
    }
}

async function fabricate_sku_recursive(req, res) {
    try {
        const response = await fabricate_sku_recursive_base(req.body.sku);
        switch (response) {
            case 0:
                res
                    .status(200)
                    .send({ message: "Se están fabricando los requerimientos" });
                break;
            case 1:
                res.status(200).send({ message: "Producto fabricado" });
                break;
            case 2:
                res.status(200).send({ message: "Producto no fabricado por nostros" });
                break;
            default:
                res.status(400).send({ message: "Ocurrió algun error" });
                break;
        }
    } catch (err) {
        console.log('LINEA 277 - FABRICATE.CONTROLLER');
        console.log(err.message);
        res.status(400).send({ message: "Ocurrió algun error" });
    }
}

module.exports = {
    fabricate_sku_recursive,
    fabricate_sku_recursive_base,
    moveItem,
    sleep,
};