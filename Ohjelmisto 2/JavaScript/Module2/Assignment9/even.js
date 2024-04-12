//Write a function called even(), which receives an array containing numbers as
// a parameter. The function returns a second (usually smaller) array which has
// the even numbers of the original array. The function must not make changes
// to the original table

'use strict';

function even(arrayOfNumbers){
  let evenArray = []
  for (let i=0 ; i < arrayOfNumbers.length; i++) {
    if (arrayOfNumbers[i] % 2 === 0) {
      evenArray.push(arrayOfNumbers[i]);
    }
  } return evenArray;
}

const randomArray = [4, 6, 9, 3, 2, 1, 120, 111, 30];
console.log(even(randomArray));