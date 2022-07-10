//validate token
var jwt = require('jsonwebtoken');  

function authenticateToken(req, res, next) {
    const token = req.body.token || req.headers['token'];
    if (token == null) return res.sendStatus(401)
  
    jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
      if (err) return res.sendStatus(403)
      req.id = user._id
      next()
    })
  };

  //export authenticateToken
  module.exports = authenticateToken;
  