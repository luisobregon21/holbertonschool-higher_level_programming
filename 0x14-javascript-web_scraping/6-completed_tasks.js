#!/usr/bin/node
// script writes a string to a file
const request = require('request');

if (process.argv.length >= 3) {
  const url = process.argv[2];
  request.get(url, function (error, response, body) {
    if (error) {
      console.error('error:', error);
    } else {
      const content = JSON.parse(body);
      const dic = {};
      let count = 0;
      for (const key in content) {
        const uId = content[key].userId;
        if (uId in dic) {
          if (content[key].completed === true) {
            count++;
          }
        } else {
          count = 0;
        }
        dic[uId] = count;
      }
      console.log(dic);
    }
  });
}
