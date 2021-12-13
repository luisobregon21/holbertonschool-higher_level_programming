#!/usr/bin/node
/*
prints a message depending of
the number of arguments passed
*/

// array containing the command-line arguments passed
const args = process.argv.length;

if (args <= 2) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
