#!/usr/bin/node

function compte (n) {
  if (n <= 1 || isNaN(n)) {
    return 1;
  }
  return n * compte(n - 1);
}

const n = parseInt(process.argv[2]);

console.log(compte(n));
