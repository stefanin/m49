const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/M49', {
    useUnifiedTopology: true, useNewUrlParser: true
})
.then(db=>{console.log('Start Data Base');})
.catch(err => console.log(err));