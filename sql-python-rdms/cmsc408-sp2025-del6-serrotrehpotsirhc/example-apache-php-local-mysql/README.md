# Apache-PHP docker-compose example

This example is primarily for development.

In this example, we use docker and docker-compose to locally host an apache/php server 
and local web page.  Further, the database is running locally in a container, initialized with the DDL-SQL file found
in the .db folder.  Finally, a phpmyadmin container is running to provide management of the database.

*./site* - this folder contains the web site.  For this example, it's a simple PHP page that lists table in a web site.

*./db* - this folder contains the SQL file used to initialize the database.  It is run once when the container is created.

*./docker-apache-php* - a docker file that creates the necessary apache-php image from the docker registry.

*./docker-compose.yml* - a docker compose file that create the docker-apache-php image, remaps our *./site* folder
to the web server root, and connects our local port 8080 to the web server port 80 inside the container.

*./env-sample* - a sample .env file.  Copy this file to `.env` and edit it as necessary.

## Folder structure

```
.\
├──db\
│   └──my-ddl.sql
├──site\
│   ├──index.php
│   └──show-table.php
├──.env
├──.env-sample
├──docker-apache-php
├──docker-compose.yml
└──README.md
```

## Create a local .env file

Docker compose can only load environment variables from a `.env` file stored IN THE SAME FOLDER as `docker-compose.yml`. To
load everything properly, you need to copy the `.env-sample` file to `.env` and then edit the `.env` file as appropriate.

Make sure that `.env` is listed in your `.gitignore` so that any `.env` files are NOT stored in your repo.

## Running the example

```shell
docker-compose up -d
```

If all goes well, you can visit: <http://localhost:8080> to see a listing tables in the HR database. `phymyadmin` will be available at <http://localhost:8081>.

