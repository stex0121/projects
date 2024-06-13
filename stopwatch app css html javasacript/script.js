const minuteslabel=document.getElementById("minutes");
const secondslabel=document.getElementById("seconds");
const milisecondslabel=document.getElementById("miliseconds");

const startButton=document.getElementById("startBtn");
const stopButton=document.getElementById("stopBtn");
const pauseButton=document.getElementById("pauseBtn");
const resetButton=document.getElementById("resetBtn");

let minutes=0;
let seconds=0;
let miliseconds=0;
let interval;

startButton.addEventListener("click",startTimer);
stopButton.addEventListener("click",stopTimer);
pauseButton.addEventListener("click",pauseTimer);
resetButton.addEventListener("click",resetTimer);

function startTimer(){
    interval=setInterval(updateTimer,10);
    startButton.disabled=true;




}

function stopTimer(){
    clearInterval(interval);
    addtoLapList();
    resetTimerData();
    startButton.disabled=false;
}

function pauseTimer(){
    clearInterval(interval);
    startButton.disabled=false;
}

function resetTimer(){
    clearInterval(interval);
    resetTimerData();
    startButton.disabled=false;


}

function updateTimer(){
    miliseconds++;
    if(miliseconds===100){
        miliseconds=0;
        seconds++;
        if(seconds===60){
            seconds=0;
            minutes++;
        }
   
    }
    displayTimer();
}

function displayTimer(){
    milisecondslabel.textContent=padTime(miliseconds);
    secondslabel.textContent=padTime(seconds);
    minuteslabel.textContent=padTime(minutes);
}

function padTime(time){
    return time.toString().padStart(2,"0");

}

function resetTimerData(){
    minutes=0;
    seconds=0;
    miliseconds=0;
    displayTimer();
}

function addtoLapList(){
    const lapTime=`${padTime(minutes)}:${padTime(seconds)}:${padTime(miliseconds)}`;
    const listItems=document.createElement("li");

    listItems.innerHTML=`<span>Lap ${lapList.childElementCount + 1}: </span>${lapTime}`;
    lapList.appendChild(listItems);
}