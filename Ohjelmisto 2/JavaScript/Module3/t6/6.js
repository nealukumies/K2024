//Open t6 folder in your IDE/editor. Make a script that opens an alert window that
// says 'Button Clicked' when the <button> element is clicked. (1p)

'use script';
function buttonAlert() {
  alert('Button clicked!');
}

button = document.querySelector('button');

button.addEventListener('click', buttonAlert);