#!/usr/bin/node
exports.esrever = function (list) {
  const size = list.length - 1;
  let newList = [];
  for (let i = size; i >= 0; i--) {
    newList = newList.concat(list[i]);
  }
  return newList;
};
