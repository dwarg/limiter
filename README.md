## Project description
This is a simple Flask application that returns the IP address of the client making the request. It includes rate limiting using Flask-Limiter to limit the number of requests per minute. It also supports different content types in the response based on the Accept header in the request. The application can be run as a Docker container. The Dockerfile includes multi-stage build to optimize the size of the image. The application also handles 404 and 500 errors with custom error pages.

The project consists of the following components:

* **app.py** - contains the source code for the Flask application, which allows users to retrieve their IP address in various formats. The file also contains limits on the number of requests to prevent excessive use of the application.
* **Dockerfile** - a Docker configuration file that allows you to build a Docker image containing the Flask application and its dependencies.

## Installation
* Clone the repository: `git clone https://github.com/dwarg/limiter.git`
* Build the Docker image: `docker build -t image_name/app:latest .`
* Push the Docker image to your Docker registry: `docker push image_name/app:latest`
* Run the container by executing the command `docker run -p 8080:8080 image_name:tag`, where image_name and tag are the name and version of the image, and 8080 is the port number on the host.

## Endpoints
The application has two endpoints:

* `'/'`: Returns the user's IP address in the requested format.
* `'/list'`: Returns a JSON object containing a list of all IP addresses that have accessed the '/' endpoint.

## TODO
* Kubernetes implementation is planned