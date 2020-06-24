const {Schema, model} = require('mongoose');

const Devices = new Schema({
    Status : {type:Number, default: 0},
    Name : { type:String},
    User : { type:String},
    IP : { type:String},
    System : { type:String},
    Serial_Number : { type:String},
    Manufacturer : { type:String},
    Model : { type:String},
    Location : { type:String},
    date: { type: Date },
    numFiles : { type:Number}

});

module.exports= model('devices',Devices,'devices');