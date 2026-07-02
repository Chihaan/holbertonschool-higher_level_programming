const addItem = document.getElementById('add_item');
const myList = document.querySelector('.my_list')
const newListElem = document.createElement('li');

addItem.addEventListener('click', function () {
  newListElem.textContent = 'Item';
  myList.appendChild(newListElem);
})
