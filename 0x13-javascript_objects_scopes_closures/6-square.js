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

  charPrint (c) {
    let size = 0;
    if (c === undefined) {
      c = 'X';
    }

    while (size < this.height) {
      // repeat returns a string that has been repeated x num of times
      console.log(c.repeat(this.width));
      size++;
    }
  }
}
// NOTE: In Node.js, each module has its own scope.

module.exports = Square;
