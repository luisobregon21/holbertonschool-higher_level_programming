#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -s -D - -o /dev/null "$1" -w '%{size_download}'
