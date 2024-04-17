//Open t10 folder in your IDE/editor. Read the first name and last name values from the
// form and print them in the <p id="target"> (2p)
// remember to stop the default action of the form
// you can use attribute selectors in querySelector() to select the <input> elements
// example output: Your name is Luke Skywalker

let button = document.querySelector('input[type="submit"]');

button.addEventListener('click', function (event) {
  event.preventDefault();
  const firstNameInput = document.querySelector('input[name="firstname"]');
  const lastNameInput = document.querySelector('input[name="lastname"]');
  const firstName = firstNameInput.value;
  const lastName = lastNameInput.value;

  document.querySelector('p').textContent = `Your name is ${firstName} ${lastName}.`;
});