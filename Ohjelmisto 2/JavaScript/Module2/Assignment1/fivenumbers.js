//Write a program that prompts the user for five numbers and prints them in
// the reverse order they were entered. Print the result to the console.(2p)
// Save the numbers to an array, then use for-loop to iterate in reverse order.
// Do not use array.reverse() function.

'use strict';

let myArray = [];

for (let i=1; i<=5; i++) {
  let number = parseFloat(prompt(`Enter ${i}. number`));
  myArray.push(number);
}

for (let i=myArray.length-1; i>=0; i--) {
  console.log(myArray[i]);
}