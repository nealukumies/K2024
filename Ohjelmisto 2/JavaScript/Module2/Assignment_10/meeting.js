//Write a voting program as described below for small-scale meeting use.
//The program asks for the number of candidates.
// Then the program asks for the names of the candidates: 'Name for candidate 1
// Store the candidates' names and initial vote count in objects like this:
//[ {
//         name: 'ellie',
//         votes: 0,
//     },
//     {
//         name: 'frank',
//         votes: 0,
//     },

'use strict';

const numberOfCandidates = parseInt(prompt('Enter how many canditates'));
let listOfCandidates = [];

for (let i = 1; i <= numberOfCandidates; i++) {
  let candidate = {
    'name': prompt(`Enter name of ${i}. candidate`),
    'votes': 0,
  };
  listOfCandidates.push(candidate);
}

//The program asks for the number of voters.
// The program asks each voter in turn who they will vote for. Voter should
// enter candidate name. If the voter enters an empty value instead of the
// voting number, it will be interpreted as an empty vote.

const numberOfVoters = parseInt(prompt('Enter how many voters'));

for (let i = 1; i <= numberOfVoters; i++) {
  let voteName = prompt(
      `Voter nr. ${i}: Enter the name of the candidate you vote for`);
  for (let candidate of listOfCandidates) {
    if (candidate.name === voteName) {
      candidate.votes ++;
      break;
    }
  }
}

function compare(a, b){
  return b.votes-a.votes;
}

listOfCandidates.sort(compare);

console.log(`The winner is ${listOfCandidates[0].name} with ${listOfCandidates[0].votes} votes.`);
console.log('Results:');
for (let candidate of listOfCandidates) {
  console.log(`${candidate.name}: ${candidate.votes} votes`);
}


// console.log(listOfCandidates);
// The program announces the name of the winner and the results by printing
// it to the console:
//The winner is pamela with 3 votes.
// results:
// pamela: 3 votes
// frank: 1 votes
// ellie: 1 votes


