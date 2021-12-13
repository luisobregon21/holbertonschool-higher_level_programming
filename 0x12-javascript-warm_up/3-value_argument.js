#!/usr/bin/node
// script prints the first argument passed to it

// first argument
const first = process.argv[2];

if (first === undefined) {
  console.log('No argument');
} else {
  console.log(first);
}
