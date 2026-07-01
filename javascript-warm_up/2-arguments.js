#!/usr/bin/node

const nb = process.argv.length
const messOne = 'No argument';
const messTwo = 'Argument found';
const messThree = 'Arguments found';

if (nb <= 2) {
  console.log(messOne);
} else if (nb === 3) {
  console.log(messTwo);
} else {
  console.log(messThree);
}
