const {Router} = require('express');
const router = Router();

const Devices = require('../models/devices');


module.exports = router;


router.get('/devices', (req,res)=>{
    
    const deviceSort = Devices.find().sort({Status: 1})
    .select()
    .then(docs =>{
        const contaRiga=docs.length;
        const idSession = Math.floor(Math.random() * 100000000000);
        //console.log(contaRiga);
        res.status(200).render('devices', {docs:docs, contaRiga:contaRiga, idSession:idSession });
    })
    .catch(err => {
        
        res.status(500).json({error: err});
    });
    

});

router.get('/devices/:id', (req,res)=>{
    const id = req.params.id;
    const deviceSort = Devices.findById(id)
    .select()
    .then(docs =>{
        let items=[]      
        items=docs.toString().replace('{','').replace('}','')
        .split('\'').join('').split(',')
        console.log(docs.toString().split(",")) 
        
        res.status(200).render('devices_id', {docs:docs, items: items});
    })
    .catch(err => {
        
        res.status(500).json({error: err});
    });
    

});






router.post('/devices-add', (req,res)=>{
    console.log(req.body);
    req.body.IP=req.ipInfo.ip; //use the source ip
    const newDevices = new Devices(req.body);
    newDevices
    .save()
    .then(result =>{
        console.log(result);
        res.status(201).send("boon add device");
    })
    .catch(err => {
        console.log();
        res.status(500).json({error: err});
    });
});
