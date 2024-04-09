//Write a program that asks the user for an integer and tells if the number is
// a prime number. (2p)
// Prime numbers are numbers that are only divisible by 1 and itself.
// For example, number 13 is a prime number as it can only be divided by 1 or 13
// so that the result is an integer.
// On the other hand, number 21 for example is not a prime number as it can be
// also be divided by numbers 3 and 7.
// Print the result on the HTML document.

'use strict';

const number = parseInt(prompt('Enter a number'));
let prime = true;
if (number === 1) {
  console.log('Number is not prime number');
} else if (number > 1) {
  for (let i = 2; i <=Math.ceil((number/2)); i++) {
    if (number % i === 0) {
      prime = false;
      break;
    }
  }
}

if (prime) {
  document.querySelector('p').textContent = `${number} is a prime number.`;
} else {
    document.querySelector('p').textContent = `${number} is not a prime number.`;
}
