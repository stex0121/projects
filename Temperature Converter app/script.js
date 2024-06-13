function ConvertTemperature(){
    const celsiusInput = document.getElementById("celsius");
    const FahrenheitInput = document.getElementById("fahrenheit");

    if (!isNaN(celsiusInput.value)) {
        const celsiusValue = parseFloat(celsiusInput.value);
        const fahrenheitValue = (celsiusValue * 9 / 5) + 32;
        FahrenheitInput.value = fahrenheitValue.toFixed(2);
    } else if (!isNaN(FahrenheitInput.value)) {
        const fahrenheitValue = parseFloat(FahrenheitInput.value);
        const celsiusValue = (fahrenheitValue - 32) * 5 / 9;
        celsiusInput.value = celsiusValue.toFixed(2);
    } else {
        alert('Please enter a valid number');   
    }
}