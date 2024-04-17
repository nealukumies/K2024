//Make an app that retrieves information about a
// TV series you enter and displays it in the console.
//API to use: TVMaze API
// First, make a valid HTML page with a search form. Example form:
// <form action="https://api.tvmaze.com/search/shows">
//   <input id="query" name="q" type="text">
//   <input type="submit" value="Search">
// </form>
// Test the form. The result should be a page full of JSON formatted data.

'use strict';

const searchForm = document.querySelector('#showSearch');
searchForm.addEventListener('submit', async function(evt) {
  // ... prevent the default action.
  evt.preventDefault();
  // get value of input element
  const inputValue = document.querySelector('#query').value;
  try {                                               // error handling: try/catch/finally
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${inputValue}`);    // starting data download, fetch returns a promise which contains an object of type 'response'
    const jsonData = await response.json();          // retrieving the data retrieved from the response object using the json() function
    console.log(jsonData);    // log the result to the console
  } catch (error) {
    console.log(error.message);
  }
});