#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return Object.assign(this, {});
    } else {
      this.width = parseInt(w);
      this.height = parseInt(h);
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

  rotate () {
    if (this.width && this.height) {
      const swap = this.width;
      this.width = this.height;
      this.height = swap;
    }
  }

  double () {
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}
module.exports = Rectangle;
