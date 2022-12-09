
 document.addEventListener("DOMContentLoaded", () => {  

    var send = document.getElementById("send"); 
    send.addEventListener("click", function(){
    
        var nombre = document.getElementById("nombre").value;
        var apepat = document.getElementById("apepat").value;
        var apemat = document.getElementById("apemat").value;
        var fecnac = document.getElementById("fecnac").value;
        var ingmens = document.getElementById("ingmens").value;
        var depec = document.getElementById("depec").value;
    
        var data = {"nombre":nombre, "apepat":apepat, "apemat":apemat, "fecnac":fecnac, "ingmens":ingmens, "depec":depec};
        console.log(data); 

    });
 });