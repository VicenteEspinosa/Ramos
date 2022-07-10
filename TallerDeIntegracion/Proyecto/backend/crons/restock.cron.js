require('dotenv').config({path: '../.env'});
var cron = require('node-cron');
const { restock_base } = require('../src/controllers/keepStock.controller');
const db = require('../src/models');


const restock_system = cron.schedule('*/15 * * * *', () => {
    console.log('Entre a cron de restock');
    restock_base();
});

const initialize = async () => {
    await db.sequelize.sync();
    restock_system.start();
    restock_base();
};

initialize();