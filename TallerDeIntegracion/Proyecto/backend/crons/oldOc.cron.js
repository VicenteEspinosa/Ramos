require('dotenv').config({path: '../.env'});
var cron = require('node-cron');
const { produceOrders } = require('../src/services/dataBase');
const db = require('../src/models');


const oc_viejas_ftp = cron.schedule('*/11 * * * *', () => {
    console.log('Se estan procesando las ordenes antiguas')
    produceOrders();
});

const initialize = async () => {
    await db.sequelize.sync();
    oc_viejas_ftp.start();
    produceOrders();
};

initialize();
