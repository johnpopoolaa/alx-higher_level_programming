#!/usr/bin/node
const { argv } = require('process');
const occurrences = Number(argv[2]);
const display = () => {
  for (let i = 0; i < occurrences; i++) {
    console.log('C is fun');
  }
};
isNaN(occurrences)
  ? (console.log('Missing number of occurrences'))
  : (display());
