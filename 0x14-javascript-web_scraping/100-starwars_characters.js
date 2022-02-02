#!/usr/bin/node
// script print all characters
const request = require('request');

if (process.argv.length >= 3) {
  const id = process.argv[2];
  const url = 'https://swapi-api.hbtn.io/api/films/' + id;
  request.get(url, function (error, response, body) {
    if (error) {
      console.error('error:', error);
    } else {
      const film = JSON.parse(body).characters;
      for (const person in film) {
        request.get(film[person], function (error, response, body) {
          if (error) {
            console.error('error:', error);
          } else {
            const peep = JSON.parse(body);
            console.log(peep.name);
          }
        });
      }
    }
  });
}
