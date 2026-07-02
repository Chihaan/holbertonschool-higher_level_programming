const toggle = document.getElementById('toggle_header');
const head = document.querySelector('header');

toggle.addEventListener('click', function () {
  if (head.classList.contains('red')) {
    head.className = ('green');
  } else {
    head.className = ('red');
  }
});
