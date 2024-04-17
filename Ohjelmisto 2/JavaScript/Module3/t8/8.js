//Open t8 folder in your IDE/editor. Make a simple calculator. (4p)
// There are two input fields where user enters numbers. Based on the drop-down list,
// calculator performs addition, subtraction, multiplication or division of these two numbers.
// Use the value attribute of <option> elements to decide which operation the calculator needs to do.
// Show the result in <p id="result"> when the button is clicked.

'use strict';

const button = document.getElementById('start');
button.addEventListener('click', ()=> {
  const num1 = parseFloat(document.getElementById('num1').value);
  const num2 = parseFloat(document.getElementById('num2').value);
  const chosenOperation = document.getElementById('operation').value;
  let result;
  switch (chosenOperation) {
    case 'add':
      result = num1 + num2;
      break;
    case 'sub':
      result = num1 - num2;
      break;
    case 'multi':
      result = num1 * num2;
      break;
    case 'div':
      result = num1 / num2;
      break;
  }
   document.getElementById('result').textContent = result.toFixed(2);
})
