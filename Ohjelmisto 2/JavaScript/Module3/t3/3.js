//Open t3 folder in your IDE/editor. Add HTML by using innerHTML property. (2p)
// Add the following HTML code to the element with id="target".
// Add the values from 'names' array to the <li> elements in a for-loop.
// <li>John</li>
// <li>Paul</li>
// <li>Jones</li>

'use strict';
const names = ['John', 'Paul', 'Jones'];


let taskTarget = document.getElementById('target');
let contents = ``;
for (let i = 0; i<names.length; i++){
  contents += `<li>${names[i]}</li>`
}

taskTarget.innerHTML = contents;