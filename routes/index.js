const {Router} = require('express');
const router = Router();

module.exports = router;

router.get('/', (req,res)=>{
    console.log('index');
    res.status(200).render('index');
});


router.get('/info', (req, res, next) => {
    res.status(200).send("M49");
    console.log(req.ipInfo.ip);
    });

router.post('/infobody', (req, res, next) => {
    console.log(req.ipInfo.ip);
    console.log(req.body);
    res.status(200).send(req.body);
    });




