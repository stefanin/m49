const {Router} = require('express');
const router = Router();

const DevicesLog = require('../models/deviceslog');

module.exports = router;





router.get('/deviceslog', (req,res)=>{
    
    const devicelogSort = DevicesLog.find().sort({date: -1})
    .select()
    .then(docs =>{
        const contaRiga=docs.length;
        const idSession = Math.floor(Math.random() * 100000000000);
        console.log(contaRiga);
        res.status(200).render('deviceslog', {docs:docs, contaRiga:contaRiga, idSession:idSession });
    })
    .catch(err => {
        
        res.status(500).json({error: err});
    });
    

});



router.post('/deviceslog-add', (req,res)=>{
    console.log(req.body);
    req.body.IP=req.ipInfo.ip.replace('::ffff:',''); //use the source ip
    const newDevicesLog = new DevicesLog(req.body);
    newDevicesLog
    .save()
    .then(result =>{
        //console.log(result);
        res.status(201).send("boon add devicelog");
    })
    .catch(err => {
        console.log(result);
        res.status(500).json({error: err});
    });
});
