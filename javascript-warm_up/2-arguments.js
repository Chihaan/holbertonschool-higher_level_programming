#!/usr/bin/node

const messOne = 'No argument';
const messTwo = 'Argument found';
const messThree = 'Arguments found';

if (process.argv.length <= 2) {
  console.log(messOne);
} else if (process.argv.length === 3) {
  console.log(messTwo);
} else {
  console.log(messThree);
}
