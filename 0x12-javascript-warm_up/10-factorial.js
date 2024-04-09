#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const firstArg = process.argv[2];
const parsedArg = parseInt(firstArg);
if (isNaN(parsedArg)) {
  console.log(1);
} else {
  const result = factorial(parsedArg);
  console.log(result);
}
