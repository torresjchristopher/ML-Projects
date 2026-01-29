# NGINX docker-compose example

This example uses docker-compose and docker to create an NGINX site with
pages mapped directly to the *./site* folder.

This example assumes that:
* you're comfortable with [docker fundamentals](https://vcu-ssg.github.io/ssg-quarto-docker-tutorial/fundamentals.html)
* you've experimented with [the static nginx example](https://github.com/vcu-ssg/ssg-quarto-docker-tutorial/tree/main/site/nginx-static-example)

*./site* contains the website files that you want to serve up.

*./Dockerfile* contains the instructions start an nginx web server.

*./docker-compose.yml* contains the instructions about where to mount the html volume and which port to watch.

*./README.md* this file!

## Learning more about NGINX and docker

* <https://www.papertrail.com/solution/guides/nginx/>
* <https://nginx.org/en/>
* <https://www.docker.com/blog/how-to-use-the-official-nginx-docker-image/>
* <https://www.youtube.com/watch?v=qNl3QRny-v4>
* <https://medium.com/@bm54cloud/docker-basics-how-to-deploy-nginx-in-a-docker-container-10b74dda5a08>
  

## Example folder structure

Below is the file structure.  If you want to run this example, you need a folder called *./site* that contains
a simple web site, and the *Dockerfile* in a folder as shown below.  The commands in this *README.md* assumes
that you're running the command in the same folder as the *Dockerfile*.

```shell
.\
│
├──site\
│   ├──index.html
│   ├──logo.png
│   ├──script.js
│   └──styles.css
│
├──Dockerfile
├──docker-compose.yml
└──README.md
```

## Running the example

```shell
docker-compose up -d
```

That's it!  The docker compose file contains all the instructions for building the container,
connecting the volumes and ports to the container, and running the container.

If it all works, you should see a web site here:  http://localhost:8080

Errors? Make sure that you stopped the previous example.  It's listing on 8080, too.


## Loading new changes or files

In our last example, we needed to rebuild the entire container if we needed to make changes to the site.  Because
we connect the container to our local filesystem, we can edit files directly.

Using VS code, make a change to the `./site/index.html` file.  Refresh the browser, and you should see your change!

In general this is a good strategy for developing your site, but is not good for deploying the site on a central server.

## Listing available containers

To see all the containers available to run, including the one you created above, use:

```shell
docker container ls --all
```

```shell
docker ps --all
```
