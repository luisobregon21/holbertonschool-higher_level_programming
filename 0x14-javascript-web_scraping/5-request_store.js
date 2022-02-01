#!/usr/bin/node
// script writes a string to a file
const request = require('request');
const fs = require('fs');

if (process.argv.length >= 4) {
  const url = process.argv[2];
  request.get(url, function (error, body) {
    if (error) {
      console.error('error:', error);
    } else {
      fs.writeFile(process.argv[3], body.body, err => {
        if (err) {
          console.error(err);
        }
      });
    }
  });
}
