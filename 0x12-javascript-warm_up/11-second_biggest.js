#!/usr/bin/node
let max = 0;
let secondBiggest = 0;
if (process.argv.length > 3) {
  process.argv.forEach(element => {
    if (element > max) {
      max = element;
    }
  });
  process.argv.forEach(element => {
    if (element < max) {
      if (element > secondBiggest) {
        secondBiggest = element;
      }
    }
  });
}
console.log(secondBiggest);
