#!/usr/bin/node
// script writes a string to a file
const process = require('process');
const request = require('request');

if (process.argv.length >= 3) {
  const url = process.argv[2];
	request.get(url, function(response) {
		else{
			console.log(`code: ${response.statusCode}`);
		}
  });
}
