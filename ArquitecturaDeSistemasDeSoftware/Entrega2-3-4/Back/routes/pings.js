var express = require("express");
var router = express.Router();
var Ping = require("../models/Ping");
var User = require("../models/User");
var Location = require("../models/Location");
const authenticateToken = require("../middleware/auth");
const amqp = require('amqplib/callback_api');
const cron = require('node-cron');

const amqpUrl = process.env.AMQP_URL || 'amqp://localhost:5672';

//get user pings
router.get("/", authenticateToken, function (req, res, next) {
  User.findById(req.id, function (err, user) {
    if (err) {
      return next(err);
    }
    res.status(200).json(user.pings);
  });
});

//create a ping
router.post("/", authenticateToken, function (req, res, next) {
  User.findById(req.id, function (err, userFrom) {
    if (err) {
      return next(err);
    }

    Ping.findOne({from: req.id, to: req.body.to}, function (err, ping) {
      if (err) {
        return next(err);
      }
      if (ping) {
        if (ping.state === "pending") {
          return res.status(400).json({
            error: "You have already sent a ping to this user",
          });
        }
        if (ping.state === "rejected" || ping.state === "approved") {
          // update ping
          ping.state = "pending";
          ping.save(function (err) {
            if (err) {
              return next(err);
            }
            res.status(200).json(ping);
          });
        }
      }
      else {
        var ping = new Ping({from: req.id, to: req.body.to, state: "pending"});
        ping.save(function (err, ping) {
          if (err) {
            return next(err);
          }
          userFrom.pings.sent.push(ping);
          userFrom.save(function (err, userFrom) {
            if (err) {
              return next(err);
            }
            User.findById(req.body.to, function (err, userTo) {
              if (err) {
                return next(err);
              }
              userTo.pings.received.push(ping);
              userTo.save(function (err, userTo) {
                if (err) {
                  return next(err);
                }
                cron.schedule('* * * * *', function () {
                  Location.findById(userFrom.locations[userFrom.locations.length -1], function (err, location) {
                    if (err) {
                      return next(err)
                    }
                    if (location === null) {
                      return next('location not found')
                    }
                    FromLocationLat = location.location.coordinates[0];
                    FromLocationLng = location.location.coordinates[1];
                    Location.findById(userTo.locations[userTo.locations.length -1], function (err, location) {
                      if (err) {
                        return next(err)
                      }
                      ToLocationLat = location.location.coordinates[0];
                      ToLocationLng = location.location.coordinates[1];
                      // calculate distance between two locations
                      var distance = Math.sqrt(Math.pow((ToLocationLat - FromLocationLat), 2) + Math.pow((ToLocationLng - FromLocationLng), 2));
                      // update ping distance
                      console.log(distance);
                      ping.distance = distance;
                      ping.save(function (err, ping) {
                        if (err) {
                          return next(err);
                        }
                      }
                      );
                    });
                  });
                });
                res.status(200).json(ping);
              });
            });
          });
        });
      }
    });
  });
});


//get ping by id
router.get("/:id", authenticateToken, function (req, res, next) {
  Ping.findById(req.params.id, function (err, ping) {
    if (err) {
      return next(err);
    }
    res.status(200).json(ping);
  });
});

// approve or reject a ping
router.put("/:id", authenticateToken, function (req, res, next) {
  const amqpUrl = process.env.AMQP_URL || 'amqp://localhost:5672';
  const fromTags = {};
  const toTags = {};
  const fromLocations = {};
  const toLocations = {};
  User.findById(req.id, function (err, user) {
    if (err) {
      return next(err);
    }
    if (user.pings.received.includes(req.params.id)) {
      // check if valid request
      Ping.findById(req.params.id, function (err, ping) {
        if (err) {
          return next(err);
        }
        console.log(ping.state);
        if (ping.state != "pending") {
          return res.status(400).json({
            error: "Ping was already resolved",
          });
        }
        // update ping
        const newState = req.body.approved === true ? "approved" : "rejected";
        ping.state = newState;
        ping.save(function (err, ping) {
          if (err) {
            return next(err);
          }
          res.status(204).json(ping);
        });
        if (newState) {
          User.findById(ping.from, function (err, userFrom) {
            if (err) {
              return next(err);
            }
            userFrom.locations.forEach(function (location) {
              Location.findById(location, function (err, location) {
                if (err) {
                  return next(err);
                }
                fromLocations[location._id] = location.location.coordinates;
                location.tags.forEach(function (tag) {
                  if (fromTags[tag]) {
                    fromTags[tag]++;
                  }
                  else {
                    fromTags[tag] = 1;
                  }
                });
              });
            });
          });
          //get locations from user to
          User.findById(ping.to, function (err, userTo) {
            if (err) {
              return next(err);
            }
            userTo.locations.forEach(function (location) {
              Location.findById(location, function (err, location) {
                if (err) {
                  return next(err);
                }
                toLocations[location._id] = location.location.coordinates;
                location.tags.forEach(function (tag) { //TODO: get tags from user to
                  if (toTags[tag]) {
                    toTags[tag]++;
                  }
                  else {
                    toTags[tag] = 1;
                  }
                });
              });
            });
          });

          // wait for locations to be found before sending
          setTimeout(function () {
            amqp.connect(amqpUrl, function(error0, connection) {
              if (error0) {
                throw error0;
              }
              connection.createChannel(function(error1, channel) {
                if (error1) {
                  throw error1;
                }
                var queue = 'ping_indices';
                var msg = JSON.stringify({
                  pingId : ping.id,
                  fromLocations: fromLocations,
                  toLocations: toLocations,
                  fromTags: fromTags,
                  toTags: toTags
                });
              
                channel.assertQueue(queue, {
                  durable: true
                });
              
                channel.sendToQueue(queue, Buffer.from(msg), {
                  persistent: true
                });
              });
            });
          }, 1000);
        }
      });
    } else {
      // invalid request
      return res.status(404).json({
        error: "Ping not found",
      });
    }
  });
});



//export router
module.exports = router;
