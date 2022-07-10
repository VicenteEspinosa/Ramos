var express = require('express');
var router = express.Router();
var Location = require('../models/Location');
var User = require('../models/User');
var Tag = require('../models/Tag');
const authenticateToken = require('../middleware/auth');


//get locations list
router.get('/', function(req, res, next) {
    Location.find({}, function(err, locations) {
        if (err) {
        return next(err);
        }
        res.status(200).json(locations);
    });
    }
);

//return a location
router.get('/:id', function(req, res, next) {
    Location.findById(req.params.id, function(err, location) {
        if (err) {
        return next(err);
        }
        res.status(200).json(location);
    });
    }
);

//create a location and add it to user's locations
router.post('/', authenticateToken, function(req, res, next) {
    Tag.find({}, function(err, tags_array) {
        if (err) {
            return next(err);
        }
        const tags = tags_array;
        User.findById(req.id, function(err, user) {
            if (err) {
            return next(err);
            }
            var location = new Location(req.body);
            location.save(function(err, location) {
                if (err) {
                return next(err);
                }
                user.locations.push(location);
                user.save(function(err, user) {
                    if (err) {
                    return next(err);
                    }
                    res.status(201).json(location);
                });
            });
            req.body.tags_tf.map((item, index) => {
                if (item) {
                    location.tags.push(tags[index]);
                    Tag.findById(tags[index].id, function(err, tag) {
                        if (err) {
                        return next(err);
                        }
                        tag.locations.push(location.id);
                        tag.save(function(err, tag) {
                            if (err) {
                            return next(err);
                            }
                        });
                    });
                }
            });
        });
    });
    }
);

//get locations of a user from username
router.get('/user/:username', function(req, res, next) {
    User.findOne({username: req.params.username}, function(err, user) {
        if (err) {
        return next(err);
        }
        if (user){
        Location.find({'_id': { $in: user.locations }}, function(err, locations) {
            if (err) {
            return next(err);
            }
            console.log(locations);
            res.status(200).json([locations]);
        })};
    });
    }
);

router.get('/api/weather', function(req, res){
    var bool = Math.random() < 0.5;
    res.status(200).json([bool]);
})

  //export router
module.exports = router;
