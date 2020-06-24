const {Schema, model} = require('mongoose');

const FilesLog = new Schema({
    Status : {type:Number, default: 0},
    date: {
        type: Date,
        // `Date.now()` returns the current unix timestamp as a number
        //default: Date.now
      },
    Name : { type:String},
    file : { type:String}

});

module.exports= model('filesLog',FilesLog,'filesLog');