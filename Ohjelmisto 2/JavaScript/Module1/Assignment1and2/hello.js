'use strict';


//1. Write a program that logs to the console this text: I'm printing to console! (1p)
console.log('I´m printing to console')

//2. Write a program that prompts for user's name and then greets the user. Print
// the result to the HTML document: Hello, Name! (2p)

const name= prompt('Enter name')
document.querySelector('p').textContent = `Hello ${name}`