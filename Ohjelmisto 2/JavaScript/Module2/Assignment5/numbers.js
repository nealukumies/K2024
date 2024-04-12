//Write a program that prompts the user for numbers. When the user enters one
// of the numbers he previously entered, the program will announce that the
// number has already been given and stops its operation and then prints all
// the given numbers to the console in ascending order.

//Write a program that asks the user for numbers until he gives zero.
// The given numbers are printed in the console from the largest to the smallest. (2p)

'use strict';

function compare(a, b) {
  return b-a;
}

let listOfNumbers = [];
let number = parseFloat(prompt('Enter number'));

while (listOfNumbers.includes(number) === false) {
  listOfNumbers.push(number);
  number = parseFloat(prompt('Enter number'));
}
alert(`${number} has already been given. End of program.`);
listOfNumbers.sort(compare);

for (let i=0; i<listOfNumbers.length; i++) {
  console.log(listOfNumbers[i]);
}




