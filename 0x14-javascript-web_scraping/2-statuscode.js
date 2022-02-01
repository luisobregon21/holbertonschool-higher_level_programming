#!/usr/bin/node
// script writes a string to a file
const process = require('process');
const request = require('request');

if (process.argv.length >= 3) {
  const url = process.argv[2];
	request.get(url, function(error, response) {
		if (error){
			console.error('error:', error);
		}
		else{
			console.log(`code: ${response.statusCode}`);
		}
  });
}
