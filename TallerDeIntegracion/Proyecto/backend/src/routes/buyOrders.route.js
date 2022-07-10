const express = require('express');
//buyOrder
const router = express.Router();
const orderController = require('../controllers/orderReception.controller');

router.post('/:id', orderController.createOrderReception);

router.patch('/:id', orderController.updateOrderReception);

module.exports = router;
