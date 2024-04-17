//Open t2 folder in your IDE/editor. Add HTML by using createElement() and
// appenChild mehtods. (2p)
// Add the following HTML code to the element with id="target"
// <li>First item</li>
// <li>Second item</li>
// <li>Third item</li>
// Add class my-item to the second list item

'use strict';

let list = document.getElementById('target');

for (let i=0; i<3; i++) {
  let li = document.createElement('li');
  list.appendChild(li);
}

document.getElementsByTagName('li')[0].innerText = 'First item';
document.getElementsByTagName('li')[1].innerText = 'Second item';
document.getElementsByTagName('li')[2].innerText = 'Third item';
document.getElementsByTagName('li')[1].className = 'my-item';
