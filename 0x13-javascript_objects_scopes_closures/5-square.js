#!/usr/bin/node
// Square class defines a square and inherits from Rectangle class

/*
 The extends keyword is used to create a child of another class
 Require is similar to import from python
 */
class Square extends require('./4-rectangle') {
  constructor (size) {
    // super is used to access and call functions on an object's parent
    super(size, size);
  }
}
// NOTE: In Node.js, each module has its own scope.

module.exports = Square;
