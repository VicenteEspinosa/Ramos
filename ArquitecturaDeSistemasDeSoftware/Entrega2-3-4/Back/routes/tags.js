var express = require('express');
var router = express.Router();
var Location = require('../models/Location');
var Tag = require('../models/Tag');
var User = require('../models/User');
const authenticateToken = require('../middleware/auth');


//get tags list
router.get('/', function(req, res, next) {
    Tag.find({}, function(err, locations) {
        if (err) {
        return next(err);
        }
        res.status(200).json(locations);
    });
    }
);

//create a tag
router.post('/', function(req, res, next) {
    var tag = new Tag(req.body);
    tag.save(function(err, tag) {
        if (err) {
        return next(err);
        }
        res.status(201).json(tag);
    });
    }
);

//delete a tag by id
router.delete('/:id', function(req, res, next) {
    Tag.findByIdAndRemove(req.params.id, function(err, tag) {
        if (err) {
        return next(err);
        }
        res.status(200).json(tag);
    });
    }
);

//get tag by id
router.get('/:id', function(req, res, next) {
    Tag.findById(req.params.id, function(err, tag) {
        if (err) {
        return next(err);
        }
        res.status(200).json(tag);
    });
    }
);


module.exports = router;