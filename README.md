# Demo Image Uploader

This is a simple Flask application that allows users to upload images and view them on a web page. It is intended for use as a proof-of-concept for demonstrating how to attach volumes to a container running on ECS or EKS.

## Usage:

To use the application, you can run it locally using Docker Compose. Simply navigate to the project directory and run the following command:

```bash
docker-compose up -d
```

This will start the application and it will be accessible at http://localhost:8889/.

A health check endpoint is available at /status. You can use this endpoint to check the health of the application. The response will be in JSON format and will include the hostname, status code, and whether the application is healthy or not.

## Configuration:

By default, the application is configured to only allow PNG, JPEG/JPG, and GIF files to be uploaded. You can change this behavior by modifying the ALLOWED_EXTENSIONS variable in app.py.

## Author:

- [@JManzur](https://jmanzur.com)