#!/usr/bin/node
// prxnts a square dependxng on the arg

const num = process.argv[2];
let x = 0;
let square = '';

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (x = 0; x < num; x++) {
    square = square.concat('X');
  }
  for (x = 0; x < num; x++) {
    console.log(square);
  }
}
