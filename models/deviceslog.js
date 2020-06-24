const {Schema, model} = require('mongoose');

const DevicesLog = new Schema({
    Status : {type:Number, default: 0},
    date: {
        type: Date,
        // `Date.now()` returns the current unix timestamp as a number
        default: Date.now
      },
    Name : { type:String},
    User : { type:String},
    IP : { type:String},
    System : { type:String},
    Serial_Number : { type:String},
    Manufacturer : { type:String},
    Model : { type:String},
    Location : { type:String},
    numFiles : { type:Number}
});

module.exports= model('deviceslog',DevicesLog,'deviceslog');