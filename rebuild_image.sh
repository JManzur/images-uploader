#!/bin/bash

IMAGE="jmanzur/images-uploader:latest"
PORT="8889"

echo "Stopping and removing container: $IMAGE"
echo ""
docker-compose down
docker rmi $IMAGE
docker build -t $IMAGE .
docker-compose up -d
echo ""
echo "Application URL: http://localhost:$PORT"
echo ""