'use strict';

const searchForm = document.querySelector('#showSearch');
let showsArray;
const resultsDiv = document.createElement('div');
resultsDiv.setAttribute('id', 'results');

searchForm.addEventListener('submit', async function(evt) {
  evt.preventDefault();
  const inputValue = document.querySelector('#query').value;

  try {
    const response = await fetch(
        `https://api.tvmaze.com/search/shows?q=${inputValue}`);
    showsArray = await response.json();
    resultsDiv.innerHTML = '';

    for (let show of showsArray) {
      let article = document.createElement('article');

      let hName = document.createElement('h2');
      hName.textContent = `${show.show.name}`;
      article.appendChild(hName);

      let showLink = document.createElement('a');
      showLink.setAttribute('href', `${show.show.url}`);
      showLink.setAttribute('target', '_blank');
      showLink.textContent = show.show.url;
      article.appendChild(showLink);

//Develop the app even further. Optional chaining is not the best way to handle missing image.
// Use ternary operator or if/else to add a default image if TV-show is missing image property. (2p)
// Use https://via.placeholder.com/210x295?text=Not%20Found as the default image.

      let imageMedium = document.createElement('img');
      imageMedium.src = show.show.image ? show.show.image.medium : 'https://via.placeholder.com/210x295?text=Not%20Found';
      imageMedium.alt = show.show.name;
      article.appendChild(imageMedium);

      let summaryDiv = document.createElement('div');
      summaryDiv.innerHTML = show.show.summary;
      article.appendChild(summaryDiv)

      resultsDiv.appendChild(article);
    }
  } catch (error) {
    console.log(error.message);
  }
});

document.body.appendChild(resultsDiv);

