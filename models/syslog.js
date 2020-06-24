const {Schema, model} = require('mongoose');

const Syslog = new Schema({
    Status : {type:Number, default: 0},
    host : { type:String},
    protocol : { type:String},
    message : { type:String},
    date: {
        type: Date,
        // `Date.now()` returns the current unix timestamp as a number
        default: Date.now
      }
});

module.exports= model('syslog',Syslog,'syslog');