#!/usr/bin/node
// script writes a string to a file
const process = require('process');
const request = require('request');

if (process.argv.length >= 3) {
  const id = 'https://swapi-api.hbtn.io/api/people/18/';
  const url = process.argv[2];
  request.get(url, function (error, response, body) {
    if (error) {
      console.error('error:', error);
    } else {
      const film = JSON.parse(body);
      const all = film.results;
      let count = 0;
      for (const i in all) {
        const list = all[i].characters;
        for (const person in list) {
          if (list[person] === id) {
            count++;
          }
        }
      }
      console.log(count);
    }
  });
}
