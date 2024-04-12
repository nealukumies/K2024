//Write a program that asks the user for numbers until he gives zero.
// The given numbers are printed in the console from the largest to the smallest. (2p)

'use strict';

function compare(a, b){
  return b-a;
}

let number;
let listOfNumbers = [];

while (number !==0) {
  number = parseFloat(prompt('Enter number'))
  if (number !== 0)
    listOfNumbers.push(number);
}

listOfNumbers.sort(compare)
for (let i = 0; i<listOfNumbers.length; i++) {
  console.log(listOfNumbers[i]);
}



