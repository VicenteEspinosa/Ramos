require('dotenv').config({path:'../.env'});
var cron = require('node-cron');
const { move_items } = require('../src/utils/moveitems');
const db = require('../src/models');


const storage_system = cron.schedule('*/10 * * * *', () => {
    console.log('Entre a cron de move_items');
    move_items();
});

const initialize = async () => {
    await db.sequelize.sync();
    storage_system.start();
    move_items();
};


initialize();
