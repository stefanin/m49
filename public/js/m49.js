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
// 2020 07 05 convert date ISO format in gg/mm/hhhh O:M:s
function FormattaData(iddata,data){
                    var dd = new Date(data);
                    document.getElementById(iddata).innerHTML = dd.toLocaleDateString('en-GB')+" "+dd.toLocaleTimeString('en-GB');

}

//2020 07 05 format the status code
function FormattaStatus(idstatus,status){ 
    if(status=="0"){
        document.getElementById(idstatus).innerHTML = status.replace("0","<span class=\"badge badge-danger\">Danger</span>");
    }
    if(status=="1"){
        document.getElementById(idstatus).innerHTML = status.replace("1","<span class=\"badge badge-warning\">Warning</span>");
    }
    if(status=="2"){
        document.getElementById(idstatus).innerHTML = status.replace("2","<span class=\"badge badge-info\">Man.</span>");
    }
    if(status=="3"){
        document.getElementById(idstatus).innerHTML = status.replace("3","<span class=\"badge badge-success\">Good</span>");
    }

}
