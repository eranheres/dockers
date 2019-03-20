#!/bin/sh
if [ -z $1 ]; then
    echo "Home mount folder is required."
    exit 1
fi
docker run -d --rm --name=roboenv -p 5901:5901 -p 6901:6901 -e VNC_PW=eranh -v $1:/headless/host roboenv
