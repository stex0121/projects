document.addEventListener("DOMContentLoaded",function(){

    const Percentageslider=document.getElementById("Percentageslider");
    const PercentageValue=document.getElementById("PercentageValue");

    Percentageslider.addEventListener("input",function(){

        PercentageValue.textContent=`${Percentageslider.value}%`;


    })
});

function calculatePercentage(){
    const Percentageslider=document.getElementById("Percentageslider").value;
    const basenumber=document.getElementById("basenumber").value;

    if(basenumber===""){
        alert("please enter a base number");
        return
    }
    const result=(parseFloat(basenumber)*parseFloat(Percentageslider)/100).toFixed(2);

    document.getElementById("result").innerHTML=`result: ${result}`;

}