#!/usr/bin/node
// class Rectangle that defines a rectangle

class Rectangle {
  // constructor must take 2 arguments w and h
  constructor (w, h) {
    /*
     If w or h is not equal to 0 and is a positive integer
     Then width and height are initialized
     */
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // instance method prints rectangle using 'X'
  print () {
    let x = 0;

    for (x = 0; x < this.height; x++) {
      // repeat returns a strunf that has been repeated x num of times
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
