//Write a program that asks for the names of six dogs. The program prints dog
// names to unordered list <ul> in reverse alphabetical order. (2p)
'use strict';

let dogArray = [];
for (let i=1; i<=6; i++){
  let dogName = prompt(`Enter ${i}. dog name`).toUpperCase();
  dogArray.push(dogName);
}

const orderedDogs = dogArray.sort();
const reversedDogs = orderedDogs.toReversed();

let list = document.getElementById('dogNames');
for (let i= 0; i<reversedDogs.length; i++) {
  let li = document.createElement('li');
  li.innerText = reversedDogs[i];
  list.appendChild(li);
}
