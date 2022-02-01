#!/usr/bin/node
// script writes a string to a file
const process = require('process');
const fs = require('fs');

if (process.argv.length > 2) {
  fs.writeFile(process.argv[2], process.argv[3], err => {
    if (err) {
      console.error(err);
    }
  });
}
