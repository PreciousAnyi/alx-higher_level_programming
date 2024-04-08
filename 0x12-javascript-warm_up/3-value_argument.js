#!/usr/bin/node
if (process.argv.slice(2)[0] === undefined) {
  console.log('No argument');
} else {
  const firstArg = process.argv.slice(2)[0];
  console.log(firstArg);
}
