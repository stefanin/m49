$(document).ready(function(){
    $("#Devices").click(function(){ GetP("#main", "/devices");});
    $("#DevicesLog").click(function(){ GetP("#main", "/deviceslog");});
    $("#Syslog").click(function(){ GetP("#main", "/syslog");});
  
  });