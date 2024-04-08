#!/usr/bin/node
const firstArg = process.argv[2];
const parsedArg = parseInt(firstArg);
if (isNaN(parsedArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsedArg}`);
}
