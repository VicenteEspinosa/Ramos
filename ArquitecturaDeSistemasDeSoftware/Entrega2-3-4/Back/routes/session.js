var express = require('express');
var router = express.Router();
var User = require('../models/User');
const { OAuth2Client } = require('google-auth-library');
const crypto = require('crypto');


async function verify(req) {
    const client = new OAuth2Client(process.env.CLIENT_ID);
    const ticket = await client.verifyIdToken({
        idToken: req.body.googleToken,
        audience: process.env.CLIENT_ID, // Specify the CLIENT_ID of the app that accesses the backend
    });
    const payload = ticket.getPayload();
    const userId = payload['sub'];
    console.log("ID: " + userId);
    return [userId, payload];
}

const removeAccents = (str) => {
    return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "")
}

const removeSpaces = (str) => {
    return str.replace(/\s/g, '')
}

//user login
router.post('/login', function(req, res, next) {
  User.findOne({ username: req.body.username }, function(err, user) {
    if (err) {
      return next(err);
    }
    if (!user) {
      return res.status(404).json({
        error: 'User not found'
      });
    }
    user.comparePassword(req.body.password, function(err, isMatch) {
      if (err) {
        return next(err);
      }
      if (!isMatch) {
        return res.status(400).json({
          error: 'Invalid password'
        });
      }
      res.status(202).json({
        token: user.generateToken()
      });
    });
  });
} );

//user register
router.post('/register', function(req, res, next) {
  const name = req.body.username;
  const mail = req.body.email;
  const pass = req.body.password;
  var user_info = {
    username: name,
    email: mail,
    password: pass,
    entityUUID: process.env.GLOBAL_ENTITYUUID,
    userUUID: crypto.randomUUID(),
    levelOnEntity: 100
  };
  User.create(user_info, function(err, user) {
    if (err) {
      return next(err);
    }
    res.status(201).json({
      token: user.generateToken()
    });
    console.log("user created");
  });
} ); 


router.post('/googleLogin', async function(req, res, next) {

    try {
        const userInfo = await verify(req)

        const [userGoogleId, payload] = userInfo

        User.findOne({ googleId: userGoogleId }, async function(err, user) {

            if (err) {
                return next(err);
            }
            if (!user) {
                console.log("Creating new user");
                try {
                    user = await User.create({
                        username: removeAccents(removeSpaces(payload.name)).replace("'",""),
                        email: payload.email,
                        googleId: userGoogleId,
                        entityUUID: process.env.GLOBAL_ENTITYUUID,
                        userUUID: crypto.randomUUID(),
                        levelOnEntity: 100
                    });
                } catch (error) {
                    console.log(error);
                    return res.status(404).json({
                        error: "Error creating user"
                    });
                }
            }
            res.status(202).json({
                token: user.generateToken()
            });
        });

    } catch (e) {
        console.log(e);
        res.status(400).json({
            error: "Invalid token"
        });
    }
});

//export router
module.exports = router;