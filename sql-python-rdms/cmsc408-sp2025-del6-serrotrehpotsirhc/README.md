# Project Deliverable 6 - template

This report supports project deliverable 6.  Deliverable 6 is all about project acceleration -
we're focusing on kickstarting development of our database and web application.

## Tasks

For this assignment we're tasked with exploring five different docker examples and preparing
a report summarizing our activities.

## Examples

The repo contains a bunch of docker examples, as listed below.  These links take you 
directly to the GITHUB repo and the respective README files.  

* [nginx-static-example](https://github.com/vcu-ssg/ssg-quarto-docker-tutorial/tree/main/site/example-nginx-static-example) - creates a simple, static web server with the html file stored inside the container.

* [nginx-static-volume](https://github.com/vcu-ssg/ssg-quarto-docker-tutorial/tree/main/site/example-nginx-static-volume) - creates a simple web server container with the html files stored on your local disk.

* [apache-php-remote-mysql](https://github.com/vcu-ssg/ssg-quarto-docker-tutorial/tree/main/site/example-apache-php-remote-mysql) - creates a local apache web server serving html/php pages from your local disk, connected to cmsc508.com using your username and password.

* [apache-php-local-mysql](https://github.com/vcu-ssg/ssg-quarto-docker-tutorial/tree/main/site/example-apache-php-local-mysql) - creates a local apache setb server serving html/php pages from your local disk, connected to a locally running mysql DB and locally running phpmyadmin.

* [production-example-1](https://github.com/vcu-ssg/ssg-quarto-docker-tutorial/tree/main/site/example-production-example-1) - creates a locally running nginx load balancer and reverse proxy, apache-php server, mysql database and phpmyadmin all talking together.

The `README.md` files in each folder provide background on the example and provide instructions for running each example.  The first two examples use `docker` commands while the last three use `docker-compose`.

## End

Thank you! We will be modifying report.qmd for this deliverable!

