#!/usr/bin/node
/*
 function converts a number from base 10
 to another base passed as argument
*/

exports.converter = function (base) {
   return function (MyConvert) {
     /*
      toString method accepts an argumentof the
      base used to convert a number into a string.
      */
    return MyConvert.toString(base);
   };
};
