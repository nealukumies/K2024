//Make an app that retrieves information about a
// TV series you enter and displays it in the console.
//API to use: TVMaze API
// First, make a valid HTML page with a search form. Example form:
// <form action="https://api.tvmaze.com/search/shows">
//   <input id="query" name="q" type="text">
//   <input type="submit" value="Search">
// </form>
// Test the form. The result should be a page full of JSON formatted data.
//Develop the app further.
// Add JavaScript that gets the value entered to the form and sends a request with
// fetch to https://api.tvmaze.com/search/shows?q=${value_from_input}.
// Print the search result to the console. (3p)

'use strict';

const searchForm = document.querySelector('#showSearch');
searchForm.addEventListener('submit', async function(evt) {
  evt.preventDefault();
  const inputValue = document.querySelector('#query').value;
  try {
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${inputValue}`);
    const jsonData = await response.json();
    console.log(jsonData);
  } catch (error) {
    console.log(error.message);
  }
});