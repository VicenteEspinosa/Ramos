const crypto = require('crypto');

const generateHash = (value) => {
  return crypto.createHmac('sha1', process.env.SECRET_KEY)
        .update(value).digest('base64')}

module.exports = {
  generateHash
}