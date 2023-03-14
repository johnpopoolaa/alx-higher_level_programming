#!/usr/bin/node

const { argv } = require('process');
if (!argv[2] || isNaN(parseInt(argv[2]))) { console.log('Not a number'); } else { console.log(`My Number: ${parseInt(argv[2])}`); }
