//Open t9 folder in your IDE/editor. This is continuation to previous task.
// There is only one text field left, where the user writes the calculation
// (addition, subtraction, multiplication or division) (4p)
// You can use the includes and split methods.
// eval() function is prohibited
// No need to support decimal numbers, calculating integers is enough.
// Example inputs: 3+5, 2-78, 3/6, etc..

'use strict';
let numbers = [];
const operators = ['+', '-', '*', '/'];
let chosenOperator;

const button = document.getElementById('start');
button.addEventListener('click', () => {
  const calculation = document.getElementById('calculation').value;
  let number = '';
  for (let i = 0; i < calculation.length; i++) {
    if (!operators.includes(calculation[i])) {
      number += calculation[i];
    } else {
      if (number !== '') {
        numbers.push(number);
        number = '';
      }
      chosenOperator = (calculation[i]);
    }
  }
  if (number !== '') {
    numbers.push(number);
  }
  let result;
  switch (chosenOperator) {
    case '+':
      result = parseInt(numbers[0]) + parseInt(numbers[1]);
      break;
    case '-':
      result = parseInt(numbers[0]) - parseInt(numbers[1]);
      break;
    case '*':
      result = parseInt(numbers[0]) * parseInt(numbers[1]);
      break;
    case '/':
      result = parseInt(numbers[0]) / parseInt(numbers[1]);
      break;
  }
   document.getElementById('result').textContent = result;
});
