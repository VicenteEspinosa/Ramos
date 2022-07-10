const Order = require('../models').Order;
const axios = require('axios');

async function createOrderReception(req, res) {
    try {
        const data = req.body;
        console.log('order received', data);
        const date = new Date();
        const day = date.getDate();
        const hour = date.getHours();
        const minutes = date.getMinutes();
        const order = await Order.create({
            internalid: `${data.cliente.slice(0, 15)}1300${day}0${hour}${minutes}`,
            cliente: data.cliente,
            sku: data.sku,
            fechaEntrega: data.fechaEntrega,
            cantidad: data.cantidad,
            urlNotification: data.urlNotification,
            state: 'recibida'
        });

        res.status(201).send({
            id: order.internalId,
            cliente: order.cliente,
            sku: order.sku,
            fechaEntrega: order.fechaEntrega,
            cantidad: order.cantidad,
            urlNotification: order.urlNotification,
            estado: order.state
        });

        await axios.patch(data.urlNotification, {
            estado: 'rechazada'});
    } catch (err) {
        res.status(400).send({message: err.message});
    }
};

async function updateOrderReception(req, res) {
    try{
        const data = req.body;
        console.log("update received", data);
        const order = await Order.findOne({
            where: {
                internalid: req.params.id
            }
        });
        if(!order) {
            res.status(404).send({message: 'No se encontro el pedido'});
        }
        await order.update({
            estado: data.estado
        });
        res.status(204).send({
            id: order.internalid,
            cliente: order.cliente,
            sku: order.sku,
            fechaEntrega: order.fechaEntrega,
            cantidad: order.cantidad,
            urlNotification: order.urlNotification,
            estado: order.state
        });
    } catch (err) {
        res.status(404).send({
            message: err.message
        })
    }
}

module.exports ={
    createOrderReception,
    updateOrderReception
}
