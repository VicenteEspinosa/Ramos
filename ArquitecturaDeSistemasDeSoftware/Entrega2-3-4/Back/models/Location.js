var mongoose = require('mongoose');
var _ = require('underscore');

//Create location schema with geoJSON type
var locationSchema = new mongoose.Schema({
    name: {type: String, lowercase: true, unique: true},
    location: {
        type: {
            type: String,
            enum: ['Point'],
        },
        coordinates: {
            type: [Number],
            required: true
        }
    },
    tags: [{type: mongoose.Schema.Types.ObjectId, ref: 'Tag'}],
    date: { type: Date, default: Date.now },
});

//location to json
locationSchema.methods.toJSON = function() {
    var location = this.toObject();
    return _.pick(location, ['_id', 'name', 'location', 'tags', 'date']);
};


//Export location schema
module.exports = mongoose.model('Location', locationSchema);

