
document.addEventListener('DOMContentLoaded', function () {
  const message = document.getElementById('hello');

  fetch('https://hellosalut.stefanbohacek.com/?lang=fr').then(function (result) {
    return result.json();
  })
    .then(function (data) {
      message.textContent = data.hello;
    });
});
