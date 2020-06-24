const {Router} = require('express');
const router = Router();

const Fileslog = require('../models/fileslog');


module.exports = router;

router.post('/fileslog-add', (req,res)=>{
    const newFileslog = new Fileslog(req.body);
    newFileslog
    .save()
    .then(result =>{
        res.status(201).send("boon add fileslog ");
    })
    .catch(err => {
        console.log();
        res.status(500).json({error: err});
    });
});
