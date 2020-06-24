var Orologino = setInterval(OrologinoTimer, 1000);

function OrologinoTimer() {
  var d = new Date();
  var t = d.toLocaleTimeString();
  var data = d.toLocaleDateString()
  document.getElementById("orologino").innerHTML = t+" "+data;
}

function wait(contenitore)
{
    switch(Math.floor(Math.random() * 3)) {
        case 0:
            var messaggio = "Wait .....";
        break; 
        case 1:
            var messaggio = "Aspetta .....";
        break; 
        case 2:
            var messaggio = "Carico .....";
        break; 
    }

    $(contenitore).html("<br><br><br><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+messaggio+"</b>");
}

function GetP(contenitore, url)
{
    wait(contenitore);
    $.get( url, function(data){
    $(contenitore).html(data);
    })
}

function mmenu(contenitore){
    alert('eccolo');
}