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
        const u_id = content[key].userId;
        const test = key + 1;
        if (u_id in dic) {
          if (content[key].completed === true) {
            count++;
          }
        } else {
          count = 0;
        }
        dic[u_id] = count;
      }
      console.log(dic);
    }
  });
}
