var mongoose = require("mongoose");
var _ = require("underscore");

// Create ping schema
var pingSchema = new mongoose.Schema({
  from: { type: mongoose.Schema.Types.ObjectId, ref: "User" },
  to: { type: mongoose.Schema.Types.ObjectId, ref: "User" },
  state: {
    type: String,
    enum: ["pending", "approved", "rejected"],
    default: "pending",
  },
  distance: { type: mongoose.Types.Decimal128, default: 0 },
  date: { type: Date, default: Date.now },
  dindin: { type: mongoose.Types.Decimal128, default: 0.0 }
});

// ping to json
pingSchema.methods.toJSON = function () {
  var ping = this.toObject();
  return _.pick(ping, ["_id", "from", "to", "state", "dindin", "distance", "date"]);
};

// Export ping schema
module.exports = mongoose.model("Ping", pingSchema);
