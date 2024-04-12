//Modify the function above so that it gets the number of sides on the dice as
// a parameter. With the modified function you can for example roll a 21-sided
// role-playing dice. The difference to the last exercise is that the dice
// rolling in the main program continues until the program gets the maximum
// number on the dice, which is asked from the user at the beginning.

'use strict';

function rollDice(n){
  return Math.floor(Math.random()*n+1);
}

const numberOfSides = parseInt(prompt('How many sides on your dice?'))

while (true) {
  let dice = rollDice(numberOfSides);
  let list = document.getElementById('diceRollList');
  let li = document.createElement(('li'));
  li.innerText = dice;
  list.appendChild(li);
  if (dice === numberOfSides) {
    break;
  }
}