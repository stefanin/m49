const M49ServerRelease ="0.5.2 build 20.7.5"
const express=require('express');
const expressip = require('express-ip');
const path=require('path');
const engine= require('ejs-mate');
var fs = require('fs');
var https = require('https');
var helmet = require('helmet');
var session = require('cookie-session');

const app=express();
console.log("M49 Server rel. "+M49ServerRelease+" id:"+Date.now());
require('./db');
require('./m49syslogServer');
//setting
const port=443;
app.use(helmet());
app.use(expressip().getIpInfoMiddleware);
app.disable('x-powered-by');
var expiryDate = new Date( Date.now() + 60 * 60 * 1000 ); // 1 hour
app.use(session({
  name: 'session',
  keys: ['key1', 'key2'],
  cookie: { secure: true,
            httpOnly: true,
            domain: 'example.com',
            path: 'foo/bar',
            expires: expiryDate
          }
  })
);

app.engine('ejs', engine);
//app.locals._layoutFile = 'default'; //this default can be overridden per request
app.set('views', path.join(__dirname,'views'));

app.set('view engine', 'ejs');
//middlewars
app.use(express.urlencoded({extended: false}));
app.use(express.json());
//routes
app.use(require('./routes/index'));
app.use(require('./routes/devices'));
app.use(require('./routes/deviceslog'));
app.use(require('./routes/syslog'));
app.use(require('./routes/fileslog'));
app.use(require('./routes/m49'));
//static
app.use(express.static(path.join(__dirname, 'public')));
//server
//app.listen(port, ()=>{
//    console.log(`server port ${port}`);
//});
https.createServer({
    key: fs.readFileSync('server.key'),
    cert: fs.readFileSync('server.cert')
  }, app)
  .listen(port, function () {
    console.log('Start HTTPS Server https://localhost:'+port+'/')
  });