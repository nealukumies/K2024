//Develop the app further (4p).
// Now add a form where you can enter a search term like in assignments 1-3
// Send the search term to https://api.chucknorris.io/jokes/search?query=${value_from_input} using fetch()
// Print each joke in this format:
// <article>
//     <p>Joke here<p>
// </article>

'use strict';

const searchForm = document.querySelector('#showSearch');
let divJokes = document.createElement('div');
searchForm.addEventListener('submit', async function(evt) {
  evt.preventDefault();
  const inputValue = document.querySelector('#query').value;
  try {
    const response = await fetch(
        `https://api.chucknorris.io/jokes/search?query=${inputValue}`);
    const jsonData = await response.json();
    console.log(jsonData);

    divJokes.innerHTML = '';

    for (let joke of jsonData.result) {
      let article = document.createElement('article');
      let paragraph = document.createElement('p');
      paragraph.innerText = joke.value;
      article.appendChild(paragraph);
      divJokes.appendChild(article);
    }

  } catch (error) {
    console.log(error.message);
  }
});

document.body.appendChild(divJokes);

