const jwt = require('jsonwebtoken');

// eslint-disable-next-line consistent-return
const userTokenProtected = async (req, res, next) => {
  try {
    const { authorization } = req.headers;
    console.log(authorization);
    const id = req.params.id || req.query.user_id;
    if (!authorization || !id) {
      return res.status(401).send({ error: 'Unauthorized' });
    }

    const payload = jwt.verify(authorization, process.env.JWT_KEY);
    if (payload.type !== 'user_token' || payload.id !== parseInt(id, 10)) {
      return res.status(403).send({ error: 'Unauthorized' });
    }
    req.user = payload;
    next();
  } catch (error) {
    console.log(error);
    if (error instanceof jwt.JsonWebTokenError) {
      return res.status(401).send({ error: 'Invalid token' });
    }
    return res.status(400).send({ error: 'Unauthorized' });
  }
};

const appTokenProtected = async (req, res, next) => {
  try {
    const { authorization } = req.headers;
    console.log(authorization);
    const id = req.params.id || req.query.app_id;
    if (!authorization || !id) {
      return res.status(401).send({ error: 'Unauthorized' });
    }
    const payload = jwt.verify(authorization, process.env.JWT_KEY);

    console.log(payload.type, payload.id, id);
    if (payload.type === 'user_token' && payload.id === parseInt(id, 10)) {
      req.scopes = ['work', 'basic', 'medical', 'education'];
      return next();
    }

    if (payload.type !== 'app_token' || payload.user_id !== parseInt(id, 10)) {
      return res.status(403).send({ error: 'Unauthorized' });
    }
    req.scopes = payload.scopes.split(',');
    next();
  } catch (error) {
    console.log(error);
    if (error instanceof jwt.TokenExpiredError) {
      return res.status(401).send({ error: 'Token expired' });
    }
    if (error instanceof jwt.JsonWebTokenError) {
      return res.status(401).send({ error: 'Invalid token' });
    }
  }
};

module.exports = {
  userTokenProtected,
  appTokenProtected,
};
