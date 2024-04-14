#!/usr/bin/node
const firstArg = process.argv[2];
if (firstArg === undefined) {
  console.log('Missing number of occurrences');
} else if (firstArg > 0) {
  for (let i = 0; i < firstArg; i++) {
    console.log('C is fun');
  }
}
