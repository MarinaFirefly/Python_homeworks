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

//take from html pseudo array (all buttons with class='btn-primary')
let listButtons = document.getElementsByClassName('btn-primary');
//for elements in listButtons
for (let i = 0; i < listButtons.length; i++){
    //if text in the button digit or '.' add in to value of output (as string)
    if ((listButtons[i].innerText < 10 && listButtons[i].innerText > -1) || listButtons[i].innerText === '.') {
    listButtons[i].onclick = ()=> {output.value+=listButtons[i].innerText};
    }
    //if text in the button equals to some operation(=,-,*,/) code changes firstNum and makes value of output equal to ''
    else if (listButtons[i].innerText === "+"||listButtons[i].innerText === "-"||listButtons[i].innerText === "*"||listButtons[i].innerText === "/"){
        listButtons[i].onclick = () => {
            firstNum += Number(output.value);
            output.value = '';
            if (listButtons[i].innerText === "+") operation = 'plus'
            else if (listButtons[i].innerText === "-") operation = 'minus'
            else if (listButtons[i].innerText === "*") operation = 'multiply'
            else if (listButtons[i].innerText === "/") operation = 'divide'
        };
    };
};

//Block for button '='
let btnEqual = document.getElementsByClassName('btn-primary')[14]
btnEqual.onclick = () => {
    secondNum = Number(output.value);
    if (operation === 'plus'){
        output.value = firstNum + secondNum;
        firstNum = 0;
    }
    else if (operation === 'minus'){
        output.value = firstNum - secondNum;
        firstNum = 0;
    }
    else if (operation === 'multiply'){
        output.value = firstNum * secondNum;
        firstNum = 0;
    }
    else if (operation === 'divide'){
        output.value = firstNum / secondNum;
        firstNum = 0;
    }
};
