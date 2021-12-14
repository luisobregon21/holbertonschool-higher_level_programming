#!/usr/bin/noode
// function returns the reversed version of a list

exports.esrever = function (list) {
  const rlist = [];
  let idx = list.length - 1;

  while (idx >= 0) {
    // push adds a new element to a list
    rlist.push(list[idx]);
    idx--;
  }
  return (rlist);
};
