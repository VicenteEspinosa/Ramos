const express = require('express');

const router = express.Router();
const storageController = require('../controllers/storage.controller');

/* POST move item between storages */
router.post('/moveItem', storageController.moveItem);

module.exports = router;
