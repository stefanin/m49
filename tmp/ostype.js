var os = require('os');

console.log(os.type()); // "Windows_NT"
console.log(os.release()); // "10.0.14393"
console.log(os.platform()); // "win32"
if (os.platform()=='linux') PingString='ping -c 1 ';
else PingString='ping -n1 ';
console.log(PingString);