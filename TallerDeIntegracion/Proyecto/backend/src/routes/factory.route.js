const express = require('express');

const router = express.Router();
const factoryController = require('../controllers/factory.controller');


/* PUT factory item request. */
router.put('/requestItem', factoryController.requestItem);

router.put('/moveStockBodega', factoryController.moveStockBodega);

module.exports = router;
