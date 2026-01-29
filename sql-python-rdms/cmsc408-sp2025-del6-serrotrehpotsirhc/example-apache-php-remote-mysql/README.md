# Apache-PHP docker-compose example

This example is primarily for development.  You would probably prefer to run nginx as a load balancer and reverse proxy,
a database locally, and a web site with files inside the container.

In this example, we use docker and docker-compose to locally host an apache/php server 
and local web page.  The web page connects to the CMSC508.COM mysql server and lists
all the tables in the HR database.

*./site* - this folder contains the web site.  For this example, it's a simple PHP page that lists table in a web site.

*./docker-apache-php* - a docker file that creates the necessary apache-php image from the docker registry.

*./docker-compose.yml* - a docker compose file that create the docker-apache-php image, remaps our *./site* folder
to the web server root, and connects our local port 8080 to the web server port 80 inside the container.

*./env-sample* - a sample .env file.  Copy this file to `.env` and edit it as necessary.

## Create a local .env file

Docker compose can only load environment variables from a `.env` file stored IN THE SAME FOLDER as `docker-compose.yml`. To
load everything properly, you need to copy the `.env-sample` file to `.env` and then edit the `.env` file as appropriate.

Make sure that `.env` is listed in your `.gitignore` so that any `.env` files are NOT stored in your repo.

## Running the example

```shell
docker-compose up -d
```

If all goes well, you can visit: <http://localhost:8080> to see a listing tables in the HR database.
