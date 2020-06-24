const SyslogServer = require("syslog-server");
const Syslog = require('./models/syslog');
const SysogSRV = new SyslogServer();
 
SysogSRV.on("message", (value) => {
    
    const newSyslog = new Syslog(value);
    newSyslog
    .save()
//    .then(result =>{
//        console.log(result);
//    })
    .catch(err => {
        console.log(result);
    });
/*
    console.log(value.date);     // the date/time the message was received
    console.log(value.host);     // the IP address of the host that sent the message
    console.log(value.protocol); // the version of the IP protocol ("IPv4" or "IPv6")
    console.log(value.message);  // the syslog message
*/
});
console.log("Start SYSLOG Server"); 
SysogSRV.start();