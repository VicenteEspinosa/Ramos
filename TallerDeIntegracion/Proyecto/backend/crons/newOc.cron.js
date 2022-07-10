require('dotenv').config({path: '../.env'});
var cron = require('node-cron');
const { executePurchaseOrders } = require('../src/services/purchaseOrdersBox');
const db = require('../src/models');


const oc_ftp = cron.schedule('*/13 * * * *', () => {
    console.log('Se estan procesando las ordenes nuevas')
    executePurchaseOrders();
});

const initialize = async () => {
    await db.sequelize.sync();
    oc_ftp.start();
    executePurchaseOrders();
};

initialize();
