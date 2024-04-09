#!/usr/bin/node
const Square5 = require('./5-square');
class Square extends Square5 {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c) {
      if (this.width && this.height) {
        const width = this.width;
        const height = this.height;
        for (let i = 0; i < height; i++) {
          console.log(`${c}`.repeat(width));
        }
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
