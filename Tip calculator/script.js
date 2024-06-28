function calculateTip(){
    const billAmount=parseFloat(document.getElementById("bill-amount").value);
    const tipPerecentage=parseFloat(document.getElementById("tip-percentage").value);

        const tipAmount=billAmount*(tipPerecentage/100);
        const totalAmount=tipAmount+billAmount;

        document.getElementById("tip-amount").textContent=`$`+tipAmount.toFixed(2);
        document.getElementById("total-amount").textContent=`$`+totalAmount.toFixed(2);




};