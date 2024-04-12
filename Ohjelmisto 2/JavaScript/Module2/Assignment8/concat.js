//Write a function called concat(), which receives an array of strings as a
// parameter. The function returns a string formed by concatenating the elements of the array.
//Example: In a four-item array, there are items Johnny, DeeDee, Joey and Marky.
// The function returns the string JohnnyDeeDeeJoeyMarky.
// Do not use array.join() function
// You can hardcode the array, no need for prompt().
// Print the result to HTML document.

'use strict';

function concat(arrayOfStrings) {
  let concatenatedArrayOfStrings = '';
  for (let i = 0; i < arrayOfStrings.length; i++) {
    concatenatedArrayOfStrings += arrayOfStrings[i];
  }
  return document.querySelector(
      'p').textContent = `${concatenatedArrayOfStrings}`;
}

const itemArray = ['Johnny','DeeDee', 'Joey', 'Marky'];
concat(itemArray);
