const trigger = document.getElementById('red_header');
const head = document.querySelector('header');

trigger.addEventListener('click', function () {
  head.classList.add('red');
});
