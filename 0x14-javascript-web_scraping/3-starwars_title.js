#!/usr/bin/node
// script writes a string to a file
const process = require('process');
const request = require('request');

if (process.argv.length >= 3) {
  const id = process.argv[2];
  request.get('https://swapi-api.hbtn.io/api/films/' + id, function (error, response, body) {
    if (error) {
      console.error('error:', error);
    } else {
      const title = JSON.parse(body);
      console.log(title.title);
    }
  });
}
