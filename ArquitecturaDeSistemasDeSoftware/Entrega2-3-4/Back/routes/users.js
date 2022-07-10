var express = require('express');
var router = express.Router();
var User = require('../models/User');
const authenticateToken = require('../middleware/auth');

//get user profile
router.get('/profile', authenticateToken, function(req, res, next) {
  User.findById(req.id , function(err, user) {
    if (err) {
      return next(err);
    }
    res.status(200).json(user);
  });
} );

//TODO: future refactor: use this function for the user profile
//returns any user's profile
router.get('/:id', function(req, res, next) {
  User.findById(req.params.id, function(err, user) {
    if (err) {
      return next(err);
    }
    res.status(200).json(user);
  });
} );

//get users list
router.get('/', function(req, res, next) {  
  User.find({}, function(err, users) {
    if (err) {
      return next(err);
    }
    res.status(200).json(users);
  });
} );

// find user by uuid
router.get('/uuid/:uuid', function(req, res, next) {
  User.findOne({userUUID: req.params.uuid}, function(err, user) {
    if (err) {
      return next(err);
    }
    res.status(200).json(user);
  });
} );

//export router
module.exports = router;
