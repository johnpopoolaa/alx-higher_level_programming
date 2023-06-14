#!/usr/bin/node
const { argv } = require('process');
const args = argv.length;

if (args === 2) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
