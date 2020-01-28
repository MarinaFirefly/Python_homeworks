//Fistly we have value of output equals to ''. It's a string. 
//Next step is adding values from buttons to output as string
//When button of some operation is pressed code remebers output and make output field empty
//When button '=' is pressed operation with existing output and value from the memory is done

//take from html document element with id "output"
let output = document.getElementById('output');
//make variables for operation(=,-,*,/) and number for further actions
let firstNum = 0;
let secondNum = 0;
let operation = '';
let currentValue = '';

//take from html pseudo array (all buttons with class='btn-primary')
let listButtons = document.getElementsByClassName('btn-primary');
//for elements in listButtons
for (let i = 0; i < listButtons.length; i++) {
    //if text in the button digit or '.' add in to value of output (as string)
    listButtons[i].onclick = () => {
        currentValue += listButtons[i].innerText
        console.log(currentValue)
        if (currentValue === '.' || (currentValue < 10 && currentValue > -1)) {
            output.value += currentValue
            currentValue = ''
        }
        else if (currentValue === '+' || currentValue === '-' || currentValue === '*' || currentValue === '/') {
            if (operation === '+') output.value = Number(firstNum) + Number(output.value)
            else if (operation === '-') output.value = Number(firstNum) - Number(output.value)
            else if (operation === '*') output.value = Number(firstNum) * Number(output.value)
            else if (operation === '/') output.value = Number(firstNum) / Number(output.value);
            firstNum = Number(output.value);
            console.log(firstNum)
            output.value = ''
            operation = currentValue
            currentValue = ''
        }

    };
};

//Block for button '='
let btnEqual = document.getElementsByClassName('btn-primary')[14]
btnEqual.onclick = () => {
    secondNum = Number(output.value);
    if (operation === '+') {
        output.value = firstNum + secondNum;
        firstNum = 0;
    }
    else if (operation === '-') {
        output.value = firstNum - secondNum;
        firstNum = 0;
    }
    else if (operation === '*') {
        output.value = firstNum * secondNum;
        firstNum = 0;
    }
    else if (operation === '+') {
        output.value = firstNum / secondNum;
        firstNum = 0;
    }
};
