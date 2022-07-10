const express = require('express');
const db = require('./src/models');
const factoryRouter = require('./src/routes/factory.route');
const stockRouter = require('./src/routes/stock.route');
const storageRouter = require('./src/routes/storage.route');
const orderRouter = require('./src/routes/oc.route');
const dashboardRouter = require('./src/routes/dashboard.route');
const ocRouter = require('./src/routes/oc.route');
const fabricateRoter = require('./src/routes/fabricateSku.route');
var cron = require('node-cron');
const { move_items } = require('./src/utils/moveitems');
const { executePurchaseOrders } = require('./src/services/purchaseOrdersBox');
const restockRouter = require('./src/routes/triggerRestock.route');
const { restock_base } = require('./src/controllers/keepStock.controller');
const { produceOrders } = require('./src/services/dataBase');

const path = require('path');
require('dotenv').config();

const app = express();

// View Engine Setup
app.set('views', './views')
app.set('view engine', 'ejs')

app.use(express.json());

app.get('/', (req, res) => {
    res.render('Home', )
});

app.use('/stocks', stockRouter);
app.use('/factory', factoryRouter);
app.use('/storage', storageRouter);
app.use('/ordenes-compra', orderRouter);
app.use('/fabricate_product', fabricateRoter);
app.use('/trigger_restock', restockRouter);


//relativo a la entrega 2
app.use('/dashboard', dashboardRouter);
app.use('/oc', ocRouter);

const PORT = process.env.PORT || 8080;
app.listen(PORT, async() => {
    console.log(`Server is running on port ${PORT}.`);
    await db.sequelize.sync();
    console.log('Database has been synced.');
});