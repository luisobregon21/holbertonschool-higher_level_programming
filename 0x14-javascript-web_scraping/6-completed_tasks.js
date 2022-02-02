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
      for (const key in content) {
        const uId = content[key].userId;
        if (!dic[uId]) {
          dic[uId] = 0;
        }
        if (content[key].completed) {
          dic[uId] += 1;
        }
      }
      const goatdic = {};
      Object.keys(dic).forEach((key) => {
        if (dic[key] > 0) {
          goatdic[key] = dic[key];
        }
      });
      console.log(goatdic);
    }
  });
}
