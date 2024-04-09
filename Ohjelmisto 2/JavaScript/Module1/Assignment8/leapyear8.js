// Write a program that prompts the user for the start and end year.
// The program prints all leap years from the interval given by the user.
// Printing is done in an unordered list to the HTML document. (3p)
'use strict';

const startYear = parseInt(prompt('Enter start year'));
const endYear = parseInt(prompt('Enter end year'));
let leapYears = [];

for (let i = startYear; i <= endYear; i++) {
  if (i % 4 === 0 && (i % 100 !== 0 || i % 400 === 0)) {
    leapYears.push(i);
  }
}

let list = document.getElementById('leapYearList');
for (let i = 0; i<leapYears.length; i++) {
  let li = document.createElement('li');
  li.innerText = leapYears[i];
  list.appendChild(li);
}
