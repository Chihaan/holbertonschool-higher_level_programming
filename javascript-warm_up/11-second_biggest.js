#!/usr/bin/node

const arg_li = process.argv.slice(2);
let nb = arg_li.map((x) => parseInt(x));
const len = nb.length;

nb = nb.sort((a, b) => a - b);

if (len < 2) {
  console.log('0');
} else {
  console.log(nb[len - 2]);
}
