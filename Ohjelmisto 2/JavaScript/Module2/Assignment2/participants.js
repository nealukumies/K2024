//Write a program that asks the user for the number of participants. After this,
// the program asks for the names of all participants. Finally, the program
// prints the names of the participants on the web page in an ordered list
// (<ol>) in alphabetical order. (2p)

'use strict';

const numberOfParticipants = parseInt(prompt('Enter number of participants'));
let participantArray = [];
for (let i=1; i<=numberOfParticipants; i++) {
  let participantName = prompt(`Enter name of ${i}. participant`).toUpperCase();
  participantArray.push(participantName);
}

const participantsOrdered = participantArray.sort();
console.log(participantsOrdered);

let list = document.getElementById('participantsList');
for (let i=0; i<participantsOrdered.length; i++) {
  let li = document.createElement('li');
  li.innerText = participantsOrdered[i];
  list.appendChild(li);
}
