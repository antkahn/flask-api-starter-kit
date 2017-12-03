# Installation

Let's begin this tutorial. You will start with cloning the repository on your local machine.

```
git clone git@github.com:antkahn/flask-api-starter-kit.git && cd flask-api-starter-kit
git co tutorial
```

Install [docker](https://docs.docker.com/engine/installation/) and [docker-compose](https://docs.docker.com/compose/install/) if you don't already have them.


## Docker

The API uses Docker in a dev environment.

Run your first command:
```
make install
```

What that command does is:
 - Docker (through docker-compose) creates the python and the DB containers as configured in the `docker-compose.yml`.
 - Docker will install Python vendors in the container through [pip](https://pip.pypa.io/en/stable/).
 The vendors to install are listed in `requirements.txt`.

FYI, the deployment command for the server does not use docker.
Vendors will be installed in a [python virtual environment](https://virtualenv.pypa.io/en/stable/) to avoid collision.

You can now start the server :

```
make start
```

You can verify that your server is running by going on the url : `http://127.0.0.1:3000/application/spec`

We now have a server to work with ! Let's code !

[Next step !](first-route.md)
