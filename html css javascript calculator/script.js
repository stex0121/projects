const element = document.getElementsByTagName('li');
const screen = document.querySelector('p');
const clear = document.getElementById('clear');

// Adding event listener to the clear button
clear.addEventListener('click', clearScreen);

// Looping through elements to add click event listeners
for (let i = 0; i < element.length; i += 1) {
    if (element[i].innerHTML === '=') {
        element[i].addEventListener("click", calculate(i));
    } else {
        element[i].addEventListener("click", addCurrentValue(i));
    }
}

// Function to perform calculation
function calculate(i) {
    return function () {
        screen.innerHTML = eval(screen.innerHTML);
    };
}

// Function to add current value to screen
function addCurrentValue(i) {
    return function () {
        if (element[i].innerHTML === "x") {
            screen.innerHTML += '*';
        } else {
            screen.innerHTML += element[i].innerHTML;
        }
    };
}

// Function to clear the screen
function clearScreen() {
    screen.innerHTML = '';
}