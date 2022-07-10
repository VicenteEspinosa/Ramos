const express = require('express');
const controllers = require("../controllers/fabricateSku.controller");

const router = express.Router();
//ruta de fabricacion
router.post('/', controllers.fabricate_sku_recursive);

module.exports = router;