# NGINX Docker Example

This is a very simple example for using NGINX to serve static web pages.  This example
assumes that you're comfortable with [docker fundamentals](https://vcu-ssg.github.io/ssg-quarto-docker-tutorial/fundamentals.html)

*./site* contains the website files that you want to serve up.

*./Dockerfile* contains the instructions to build and run a nginx website on *localhost:8080*

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
└──README.md
```


## Building the container

Before you can run a container you need to build it.  The following command
will build a container using the *Dockerfile* found in the current *.* directory.

The container will be assigned the *tag* (`-t`) *nginx-test* so that it is easier to reference later.

```shell
docker build -t nginx-test .
```

## Listing available images

```shell
docker images
```

## Listing available containers

To see all the containers available to run, including the one you created above, use:

```shell
docker container ls --all
```

```shell
docker ps --all
```

## Running an image

A image is run with a simple *docker run* command.  However, if you want to interact with
the container, we need to provide more detailed instructions on how it is to interact with our 
computer.  Otherwise, it will run completely isolated with no interactions with us!

When you type `docker run`, Docker first checks if the specified image exists locally; if not, it pulls the image from a registry like Docker Hub. Once the image is available, Docker creates a new container from the image, assigning it an isolated environment with its own file system, network interface, and processes. Finally, the container starts running, executing the command defined in the image or the one you specified in the `docker run` command.

```shell
docker run -d -p 8080:80 nginx-test
```

*-d* instructs docker to run this container detached from the current shell.  This will
keep your container running until you kill the running container,
you stop docker, or your machine reboots.

*-p* instructs docker to attach local port *8080* to port *80* in the container.  Browser requests sent to *localhost:8080* will be passed to the container through port *80*.

*nginx-test* is the human name of image from above.  Docker will use local images first, and if not found, try to load an image from the docker registry.

## Testing the web site

If all went well, your website is available at <http://localhost:8080>

## Listing containers available or running

To see all the containers available to run, including the one you created above, use:

```shell
docker container ls --all
```

```shell
docker ps --all
```
## Stopping the container

```shell
docker stop <name>
```
*name* is either the `ID` of the container or the `name` of the container
from the list.

## Loading new changes or files

To load changes to the web site or configuration changes in how the container runs, you need to create a new container.
Containers are monolithic, that is, you can't make changes to a container after it's built.  You can only stop it, re-run it, or delete it.

To make changes to your web site:

1. *stop* the existing container,
2. *delete* the existing container, 
3. *edit* the files in the *site* folder,
4. *build* the container with any changes (see above),
5. *run* the new container (see above)
