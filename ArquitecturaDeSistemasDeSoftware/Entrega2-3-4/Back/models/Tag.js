var mongoose = require('mongoose');
var _ = require('underscore');

//Create tag schema with geoJSON type
var tagSchema = new mongoose.Schema({
    name: {type: String, lowercase: true, unique: true},
    locations: [{type: mongoose.Schema.Types.ObjectId, ref: 'Location'}],
    date: { type: Date, default: Date.now },
});

//tag to json
tagSchema.methods.toJSON = function() {
    var tag = this.toObject();
    return _.pick(tag, ['_id', 'name', 'locations', 'date']);
};


//Export tag schema
module.exports = mongoose.model('Tag', tagSchema);