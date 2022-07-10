const express = require('express');
const controllers = require("../controllers/keepStock.controller");

const router = express.Router();
//ruta de fabricacion
router.get('/', controllers.restock);

module.exports = router;