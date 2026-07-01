#!/usr/bin/node

const nb = process.argv.length;

if (nb <= 2) {
  console.log('No argument');
} else if (nb === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
