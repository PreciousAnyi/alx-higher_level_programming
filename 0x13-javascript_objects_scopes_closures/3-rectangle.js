#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return Object.assign(this, {});
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      const width = this.width;
      const height = this.height;
      for (let i = 0; i < height; i++) {
        console.log('X'.repeat(width));
      }
    }
  }
}
module.exports = Rectangle;
