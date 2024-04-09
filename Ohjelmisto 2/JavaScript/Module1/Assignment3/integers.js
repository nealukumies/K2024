// 3.Write a program that prompts for three integers. The program prints the sum,
// product and average of the numbers to the HTML document. (3p)
// remember to convert strings to numbers when adding

'use strict';

const num1 = parseFloat(prompt('Insert number'))
const num2 = parseFloat(prompt('Insert another number'))
const num3 = parseFloat(prompt('Insert third number'))

const sum = num1 + num2 + num3
const product = num1 * num2 * num3
const average = (sum/3).toFixed(2)

document.querySelector('p').textContent = `Sum of your numbers is ${sum}. Product is ${product}. Average is ${average}.`

