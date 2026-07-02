const listMovie = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json').then(function (result) {
  return result.json();
})
  .then(function (data) {
    data.results.forEach(function (movie) {
      const liElement = document.createElement('li');
      liElement.textContent = movie.title;
      listMovie.appendChild(liElement);
    });
  });
