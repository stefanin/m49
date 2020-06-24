const {Router} = require('express');
const { exec } = require("child_process");
const router = Router();
const os = require('os');
const fs = require('fs');
const { nextTick } = require('process');
module.exports = router;

//verify the os type and configuring the ping option
if (os.platform()=='linux') PingString='ping -c 1 ';
else PingString='ping -n 1 ';

//
router.get('/mmenu/:contenitore&:name&:ip&:id', (req,res)=>{
    const contenitore = req.params.contenitore;
    const name = req.params.name;
    const ip = req.params.ip;
    const id = req.params.id;

    console.log('mmenu');
    res.status(200).render('mmenu',{contenitore:contenitore, name:name, ip:ip, id:id });
});
router.get('/ping/:ip', (req,res)=>{
    const ip = req.params.ip;

    exec(PingString+ip, (error, stdout, stderr) => {
        if (error) {
            //console.log(`error: ${error.message}`);
            res.status(200).send("<pre>failed to ping "+ip+"</pre>");
            return;
        }
        if (stderr) {
            //console.log(`stderr: ${stderr}`);
            res.status(200).send("<pre>failed to ping "+ip+"</pre>");
            return;
        }
        //console.log(`stdout: ${stdout}`);
        res.status(200).send("<pre>"+stdout+"</pre>");
    });
});
router.get('/nmap/:ip', (req,res)=>{
    const ip = req.params.ip;

    exec("nmap -sT -Pn -vv "+ip+" --exclude-ports 860,3260", (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            res.status(200).send("<pre>failed to ping "+ip+"</pre>");
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            res.status(200).send("<pre>failed to ping "+ip+"</pre>");
            return;
        }
        console.log(`stdout: ${stdout}`);
        res.status(200).send("<pre>"+stdout+"</pre>");
    });
});

router.get('/download/:idfile', function(req, res, next){
    const idfile = req.params.idfile;
    console.log(idfile);
    const file = `${__dirname}/../public/download/`+idfile;
    if(fs.existsSync(file)){
        res.download(file); // send file 
      }else{
        console.log(file+" file not exist !!");
        res.status(501).send("<script> alert(\""+file+" file not exist !!\");</script> <meta http-equiv=\"Refresh\" content=\"0; url='/'\" />");

      }
    
  });