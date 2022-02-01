#!/usr/bin/node
 // script writes a string to a file
const process = require("process");
const request = require("request");

if (process.argv.length === 3) {
    const url = process.argv[2];
    request.get(url).on("response", function(response) {
        console.log(`code : ${response.statusCode}`); // 200
        console.log(response.headers["content-type"]); // 'image/png'
    });
}