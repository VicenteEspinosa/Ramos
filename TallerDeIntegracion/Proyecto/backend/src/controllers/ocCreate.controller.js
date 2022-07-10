const axios = require('axios');
const { ocClient } = require('../services/mainServer');
const gruposDev = require("../utils/groupsocDesarrollo.json");
const gruposProd = require("../utils/groupsocProduccion.json");
const colors = require('colors')

async function createOrder(sku, amount, group_id) {
    try {
        const grupos = process.env.PRODUCTION ? gruposProd : gruposDev;
        const url = grupos[`${group_id}`]['url'];
        const id_supplier = grupos[`${group_id}`]['id_oc'];
        const id_client = grupos['13']['id_oc'];
        const date = Date.now();
        const date_delivery = date + 2 * 3600 * 1000;

        const order = await ocClient.put('/crear', {
            cliente: id_client,
            proveedor: id_supplier,
            sku: sku,
            fechaEntrega: date_delivery,
            cantidad: amount,
            precioUnitario: 824,
            canal: 'b2b'
        });
        const id_oc = order.data['_id'];
        console.log(`OC ${id_oc} creada en nuestra base de datos`.green);
        const response = await axios.post(`${url}/ordenes-compra/${id_oc}`, {
            cliente: id_client,
            sku: sku,
            fechaEntrega: date_delivery,
            cantidad: amount,
            urlNotificacion: " "
        }, {
            "timeout": 3000,
        });
        if (response.status === 201) {
        console.log(`OC ${id_oc} creada exitosamente en el grupo ${group_id}`.green);
        } else {
            console.log(`OC ${id_oc} no se pudo crear en el grupo ${group_id}`.red);
            console.log(`Error code del otro grupo: ${response.status}`.red);
        }
        return true
    } catch (error) {
        console.log(`Error creando OC ${sku}`.red);
        console.log(error.message);
        return false
    }
}

module.exports = {
    createOrder,
};