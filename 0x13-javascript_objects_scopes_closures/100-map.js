#!/usr/bin/node
// script imports an array and computes a new array.

const list = require('./100-data.js').list;
console.log(list);

/*
 The map() method creates a new array populated with
 the results of calling a provided function on every
 element in the calling array.
 */

let idx = 0;
const newList = list.map(x => x * idx++);
console.log(newList);
