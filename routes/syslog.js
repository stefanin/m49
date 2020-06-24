const {Router} = require('express');
const router = Router();

const Syslog = require('../models/syslog');

module.exports = router;

router.get('/syslog', (req,res)=>{
    
    const syslogSort = Syslog.find()
    .sort({date: -1})
    .limit(512)
    .select()
    .then(docs =>{
        const contaRiga=docs.length;
        const idSession = Math.floor(Math.random() * 100000000000);
        console.log(contaRiga);
        res.status(200).render('syslog', {docs:docs, contaRiga:contaRiga, idSession:idSession });
    })
    .catch(err => {
        
        res.status(500).json({error: err});
    });
    

});




