#!/usr/bin/node
// function returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  /*
   for...of access the element itself
   for...in access the index of the elemenet
   */

  for (const element of list) {
    if (element === searchElement) {
      count++;
    }
  }

  return (count);
};
