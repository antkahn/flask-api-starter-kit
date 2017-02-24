# Installation

Let's begin this tutorial. You will start with cloning the repository on your local machine.

```
git clone git@github.com:antkahn/flask-api-starter-kit.git && cd flask-api-starter-kit
git co tutorial
```

Install [docker](https://docs.docker.com/engine/installation/), [docker-compose](https://docs.docker.com/compose/install/) and [npm](https://docs.npmjs.com/getting-started/installing-node) if you don't already have them.

Run

```
npm install
```

to install the necessary npm packages.
You will now have access to all the commands listed [here](https://github.com/antkahn/flask-api-starter-kit#commands) by running

```
npm run <command>
```

## Docker

The API uses Docker in a dev environment.

Run your first command:
```
npm run server:install
```

What that command does is:
 - Docker (through docker-compose) creates the python and the DB containers as configured in the `docker-compose.yml`.
 - Docker will install Python vendors in the container through [pip](https://pip.pypa.io/en/stable/).
 The vendors to install are listed in `requirements.txt`.

FYI, the deployment command for the server does not use docker.
Vendors will be installed in a [python virtual environment](https://virtualenv.pypa.io/en/stable/) to avoid collision.

You can now start the server :

```
npm run server:up
```

You can verify that your server is running by going on the url : `http://127.0.0.1:5053/application/routes`
As you can see, you already have some configured routes : `status`, `ping` and `routes`.
What those do are pretty self explanatory.

We now have a server to work with ! Let's code !

## Python

It is very important that you write clean python code, so everybody can understand what you do.

For that, be sure to install one (or more) python linter on your machine.
The PEP8 python linter will check that you respect the style standards of python : [PEP8](https://www.python.org/dev/peps/pep-0008/).
Another python linter is Flake8 that does about the same, but also checks for unused / undefined variables.

For example, if you are using Atom and MacOS, run:

```
apm install linter linter-pep8
pip install pep8
```

More of a Linux guy ? We got you covered !
```
sudo apt-get install pep8
apm install linter linter-pep8
```

Depending on your python setup, you might need to use the super user rights to install PEP8.

[Next step !](first-route.md)
