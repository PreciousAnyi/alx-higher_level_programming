#!/usr/bin/node
let max = 0;
let secondBiggest = 0;
if (process.argv.length > 3) {
  process.argv.forEach(element => {
    const parsedElement = parseInt(element);
    if (parsedElement > max) {
      max = parsedElement;
    }
  });
  process.argv.forEach(element => {
    const parsedElement = parseInt(element);
    if (parsedElement < max && parsedElement > secondBiggest) {
      secondBiggest = element;
    }
  });
}
console.log(secondBiggest);
