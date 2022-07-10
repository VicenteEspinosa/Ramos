const express = require('express');

const router = express.Router();
const ocController = require('../controllers/oc.controller');

/* GET stock */
router.get('/', ocController.get);

router.post('/:id', ocController.post);

router.patch('/:id', ocController.patch);

module.exports = router;