#!/usr/bin/node
// Computes a dictionary of user ids by occurrence.

// rquire() is a built-in function with a special purpose: to load modules.
const dict = require('./101-data').dict;
const newdict = {};
for (const key in dict) {
  if (newdict[dict[key]] === undefined) {
    newdict[dict[key]] = [];
  }
  newdict[dict[key]].push(key);
}

console.log(newdict);
