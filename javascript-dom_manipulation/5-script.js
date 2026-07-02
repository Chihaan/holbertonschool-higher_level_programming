const trigger = document.getElementById('update_header');
const head = document.querySelector('header');

trigger.addEventListener('click', function () {
  head.textContent = 'New Header!!!';
});
