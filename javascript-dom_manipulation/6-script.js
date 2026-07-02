const hero = document.getElementById('character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json').then(function (result) {
  return result.json()
})
.then(function (data) {
  hero.textContent = data.name;
});
