const button=document.getElementById("copy");
const main_paragraph=document.getElementById("main_paragraph");
const message=document.getElementById("message");

function copytoClipboard(element){

navigator.clipboard.writeText(element.textContent).then(()=>{
    message.textContent="Copy to Clipboard";
    message.classList.add("after-clicked");
})
.catch((err)=>{
    console.log("Unable to copy the data");
})
.finally(()=>{
    setTimeout(()=>{
        message.textContent="";
        message.classList=remove("after-clicked");
    },2000);
});



}

button.addEventListener("click",()=>copytoClipboard(main_paragraph));