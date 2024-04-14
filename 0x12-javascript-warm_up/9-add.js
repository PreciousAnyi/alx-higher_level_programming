#!/usr/bin/node
const firstArg = process.argv[2];
const secondArg = process.argv[3];
function addArgs (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
if (isNaN(firstArg) || isNaN(secondArg)) {
  console.log('NaN');
} else {
  addArgs(firstArg, secondArg);
}
