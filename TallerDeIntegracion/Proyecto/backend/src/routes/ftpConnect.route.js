const express = require('express');
const ftpController = require('../controllers/ftp.controller');

const router = express.Router();
//ftp
router.get('/', ftpController.FTPConnect );

module.exports = router;