const Client = require('ssh2-sftp-client');
const sftp = new Client();
const fs = require('fs');
const parser = require('xml2json');
const _ = require('underscore');
require('dotenv').config({ path: '../../.env' });
const { ocClient } = require('../services/mainServer');
const Order = require('../models').Order;
const { sleep } = require('../controllers/fabricateSku.controller');
const colors = require('colors');

const executePurchaseOrders = async() => {
    console.log("Executing purchase orders".yellow);
    const orders = await getPurchaseOrders();
    console.log('ORDENES');
    console.log(orders);
    if (orders.length === 0) {
        console.log("No hay ordenes para procesar".blue);
        return;
    }
    for (const order of orders) {
        if (!order) {
            continue;
        }
        try {
            newOrder = await Order.create({
                internalid: order[0]._id,
                cliente: order[0].cliente,
                fechaentrega: order[0].fechaEntrega,
                sku: order[0].sku,
                cantidad: order[0].cantidad,
                urlnotificacion: order[0].urlNotificacion,
                state: 'recibida',
                canal: 'ftp',
            });
            console.log(`Order ${newOrder.internalid} created`.green);
        } catch (error) {
            console.log(`Error creating order ${order[0]._id}`.red);
            console.log(error.message);
        };
    }

    for (const order of orders) {
        if (!order) {
            continue;
        }
        try {
            if (new Date(order[0].fechaEntrega) < new Date()) {
                console.log()
                await ocClient.post(`/rechazar/${order[0]._id}`, {
                    rechazo: 'Se rechaza por fecha vencida'
                }, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                console.log(`OC ${order[0]._id} rechazada por fecha vencida`.red);
                await Order.update({ state: 'rechazada' }, { where: { internalid: order[0]._id } });
                console.log(`OC ${order[0]._id} actualizada a rechazada`.green);
            } else {
                await ocClient.post(`/recepcionar/${order[0]._id}`, {}, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                console.log(`OC ${order[0]._id} aceptada`.green);
                await Order.update({ state: 'aceptada' }, { where: { internalid: order[0]._id } });
            }
        } catch (error) {
            console.log(`Error en aceptacion/rechazo de oc ${order[0]._id}`.red);
            console.log(error.message)
        }
    }
}

const getPurchaseOrders = async() => {
    try {
        await sftp.connect({
            host: 'ensalada.ing.puc.cl',
            port: '22',
            username: process.env.PRODUCTION ? 'grupo13_produccion' : 'grupo13_desarrollo',
            password: process.env.SFTP_PASSWORD
        });
        const file_list = await sftp.list('/pedidos');
        console.log("FTP FILES ============================================");
        console.log(file_list);
        for (const item of file_list) {
            const dst = fs.createWriteStream(`./${item.name}`);
            if (item.name.endsWith('.xml')) {
                await sftp.get(`./pedidos/${item.name}`, dst);
                console.log(`${item.name} downloaded`);
                await sftp.delete(`./pedidos/${item.name}`);
                console.log(`${item.name} deleted`);
            }

        }
        await sftp.end();
        console.log('succesfully closed sftp connection');
        const files = fs.readdirSync('./');
        const orders = [];
        for (const file of files) {
            if (file.endsWith('.xml')) {
                const xml = fs.readFileSync(file, 'utf8');
                const json = parser.toJson(xml);
                const jsonParsed = JSON.parse(json);
                fs.unlinkSync(`./${file}`);
                orders.push(jsonParsed);
            }
        }
        const orderData = [];
        for (const order of orders) {
            const data = await ocClient.get(`/obtener/${order.order.id}`, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            orderData.push(data.data);
        }
        console.log(`Finished obtaining orders, number of orders ${orderData.length}`.green);
        await sleep(3000);
        return orderData
    } catch (error) {
        console.log(error.message);
        return []
    }
}

module.exports = {
    executePurchaseOrders
}