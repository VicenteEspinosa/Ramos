const express = require('express');

const router = express.Router();
const dashboardController = require('../controllers/dashboard.controller');

/* GET stock */
router.get('/', dashboardController.get);

module.exports = router;
