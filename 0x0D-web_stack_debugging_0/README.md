# Docker and Apache Setup

This guide covers how to run a Docker container from an image, install Apache in the container, and serve a simple web page.

## Pulling a Docker Image

First, you need to pull the Docker image from a Docker registry. In this case, we used Docker Hub:

```bash
docker pull holbertonschool/265-0
```

## Running a Docker Container

After pulling the image, you can run it to create a new Docker container:

```bash
docker run -p 8080:80 -d -it holbertonschool/265-0
```

This command maps port 8080 on your host machine to port 80 on the Docker container.

## Checking Docker Container ID

You can check your Docker container ID by using the `docker ps` command:

```bash
docker ps
```

## Connecting to a Docker Container

To connect to the running Docker container, use the `docker exec` command followed by the container ID:

```bash
docker exec -it <container-id> /bin/bash
```

Replace `<container-id>` with your actual Docker container ID.

## Installing Apache in the Docker Container

Once you're inside the Docker container, you can install Apache:

```bash
apt-get update
apt-get install apache2 -y
```

## Creating a Web Page

After installing Apache, create a new `index.html` file in the Apache document root (`/var/www/html/`) with the content "Hello Holberton":

```bash
echo "Hello Holberton" > /var/www/html/index.html
```

## Starting the Apache Service

Finally, start the Apache service:

```bash
service apache2 start
```

Now, if you exit the Docker container and curl port 8080 on your host machine, you should see "Hello Holberton".

Please note that these commands are for a Debian-based Docker image. If your Docker image is based on a different Linux distribution, the commands might be slightly different. 
