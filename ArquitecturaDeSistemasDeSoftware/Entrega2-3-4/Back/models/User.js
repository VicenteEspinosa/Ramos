var mongoose = require('mongoose');
var bcrypt = require('bcrypt');
var jwt = require('jsonwebtoken');
var _ = require('underscore');

//Create user schema
var userSchema = new mongoose.Schema({
  username: {type: String, lowercase: true, unique: true, required: [true, "can't be blank"], match: [/^[a-zA-Z0-9]+$/, 'is invalid'], index: true},
  email: {type: String, lowercase: true, unique: true, required: [true, "can't be blank"], match: [/\S+@\S+\.\S+/, 'is invalid'], index: true},
  entityUUID: {type: String, required: true},
  userUUID: {type: String, required: true},
  levelOnEntity: {type: Number, required: true},
  password: String,
  locations: [{type: mongoose.Schema.Types.ObjectId, ref: 'Location'}],
  pings: {
    sent: [{type: mongoose.Schema.Types.ObjectId, ref: 'Ping'}],
    received: [{type: mongoose.Schema.Types.ObjectId, ref: 'Ping'}],
  },
  date: { type: Date, default: Date.now },
  googleId: { type: String, required: false },
});

//Hash password before saving
userSchema.pre('save', function(next) {
  var user = this;
  if (!user.isModified('password')) return next();
  bcrypt.hash(user.password, 10, function(err, hash){
    if (err) return next(err);
    user.password = hash;
    next();
  });
});

//Compare password in database and password the user entered
userSchema.methods.comparePassword = function(password, done) {
  bcrypt.compare(password, this.password, function(err, isMatch) {
    done(err, isMatch);
  });
};

//Generate token for user
userSchema.methods.generateToken = function() {
  var user = this;
  var token = jwt.sign({entityUUID: user.entityUUID, userUUID: user.userUUID, levelOnEntity: user.levelOnEntity, _id: user._id}, process.env.JWT_SECRET, {expiresIn: '7 days'});
  return token;
};

//get json of user with locatoins
userSchema.methods.toJSON = function() {
  var user = this.toObject();
  return _.pick(user, ['_id', 'username', 'email', 'entityUUID', 'userUUID', 'levelOnEntity', 'locations', 'pings', 'date']);
};




//export module
module.exports = mongoose.model('User', userSchema);