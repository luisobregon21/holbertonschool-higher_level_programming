#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -o /dev/null -s -w "%{http_code}" $1
