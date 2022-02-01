#!/usr/bin/node
// script reads and prints the content of a file.
const process = require('process');
const fs = require('fs');

if (process.argv.length === 3) {
  fs.readFile(process.argv[2], 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}
