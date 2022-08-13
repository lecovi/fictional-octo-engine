# fictional-octo-engine

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

A simple Flask application for demo Docker and its usage in a Python environment.

Every version is built on top of the previous one. Keep reading to get more details.

## :thinking: Why this is called "fictional-octo-engine"?

We know that naming things is hard. So, to be honest with you, this app is called like
that because I didn't wanna think so much, so I took the name that Github was
suggesting me when I was creating this repository :rofl:.

## :checkered_flag: Summary

- :octocat: [v0.1.0 - App with Poetry](https://github.com/lecovi/fictional-octo-engine/tree/feature/v0.1.0)
    - :information_source: [details](#v010---simple-flask-app-with-poetry)
- :octocat: [v0.2.0 - App with Poetry and Docker](https://github.com/lecovi/fictional-octo-engine/tree/feature/v0.2.0)
    - :information_source: [details](#v020---app-with-poetry-and-docker)
- :octocat: [v0.3.0 - App with another Python Version](https://github.com/lecovi/fictional-octo-engine/tree/feature/v0.3.0)
    - :information_source: [details](#v030---app-with-another-python-version)
- :octocat: [v0.4.0 - App with Poetry and Docker Compose](https://github.com/lecovi/fictional-octo-engine/tree/feature/v0.4.0)
    - :information_source: [details](#v040---app-with-poetry-and-docker-compose)
- :octocat: [v0.5.0 - App with a Redis service](https://github.com/lecovi/fictional-octo-engine/tree/feature/v0.5.0)
    - :information_source: [details](#v050---app-with-a-redis-service)
- :octocat: [v0.6.0 - App with Poetry insider Docker](https://github.com/lecovi/fictional-octo-engine/tree/feature/v0.6.0)
    - :information_source: [details](#v060---app-with-poetry-inside-docker)
- :octocat: [v0.7.0 - App with better project structure](https://github.com/lecovi/fictional-octo-engine/tree/feature/v0.7.0)
    - :information_source: [details](#v070---app-with-better-project-structure)
- :octocat: [v0.8.0 - App with tests](https://github.com/lecovi/fictional-octo-engine/tree/feature/v0.8.0)
    - :information_source: [details](#v080---app-with-tests)

# :mag: Versions

## v0.1.0 - Simple Flask App with Poetry

A little bit more complex than the [https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application](minimal application from official docs).
This version uses a hello-world like approach. Reads values from ENVVARS and uses them
on the response.

## v0.2.0 - App with Poetry and Docker

This version has the same functionality as before. It only adds a [Dockerfile](https://docs.docker.com/engine/reference/builder/) to run the
application with [Docker](https://docs.docker.com/get-started/).
Before running your app with a docker container, you have to build your Docker Image.
The docker image uses an official Python Docker Image. And the official Python Docker
Image doesn't have poetry support. That's why there is a `requirements.txt` file. 
The `requirements.txt` file was exported with `poetry`: 

```bash
$ poetry export --format requirements.txt --without-hashes --output requirements.txt
```

We use `--without-hashes` flag to avoid problems with some packages that may not
provide a hash to check. 
We are able to run this version using `poetry` or `docker`. 

## v0.3.0 - App with another Python Version

Now, using Docker, it's pretty easy to change something like the Python version that we
use to run our app. There is no need to install a new python version onto your system.
That's one of the benefits we have for using Docker containers.
We can easily use a python release candidate version and check if everything will work
fine with the new incoming release. 

We can get inside the running container and check that the python version that is
running is the python version that we defined in our Dockerfile and not the one that 
our system has.

```bash
$ docker exec -ti fictional-octo-engine sh
/usr/src/app # python
Python 3.10.6 (main, Aug  3 2022, 10:57:21) [GCC 11.2.1 20220219] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## v0.4.0 - App with Poetry and Docker Compose

Instead of constantly executing long docker commands we can use `docker compose` to run
our containers. This version adds the `docker-compose.yml` file that `docker compose` 
uses to run the containers. Check [official docs](https://docs.docker.com/compose/) to 
get more details.

If we a take a closer look to the repository we can see that the flask app didn't change
its functionality. This version has the same functionality that the first one has.

Now it's even easier to get into the containers. We only have to remember which name 
we gave them in the `docker-compose.yml` file. In our case we name it `app`. 

```bash
docker compose exec app sh
``` 

## v0.5.0 - App with a Redis service

Now that we are using `docker compose` is pretty easy to add new services to our app.
We just need to define them in the `docker-compose.yml` file with proper configuration.

For example, in this version, we use a [Redis](https://redis.io/) (a in-memory key:value
 DB) to add new functionality into our app. We simply add some values to some keys and
we expose and endpoint with the Flask app to query those keys.

## v0.6.0 - App with Poetry inside Docker

After running several version of this app with docker we probably noticed that some 
files belong to the `root` user. That's because inside the docker container the default 
user is `root`. 
And in a normal workflow if we add dependencies with `poetry` to have them installed 
inside our docker container we need to export them into a `requirements.txt` file. 
So, let's make a simple change here: install `poetry` and change to a non-priviled user.

## v0.7.0 - App with better project structure

Having a single file containing the whole Flask app isn't a good practice. So, in this
version we take advantage of the Flask's Blueprints functionality to modularize our app.

We are not adding new functionality to the Flask application. We are making our app more
sustainble. Trust me, this is a great way to go.

## v0.8.0 - App with tests

In the previous version we were focused on sustainability. So, let's go deeper on that.
In this version we add a few tests to gain more trust on our application with the 
incoming new functionalities. Adding tests will provide your app a way to check if
everything still working as expected when you change something in your codebase.

## v0.9.0 - App with tests AND coverage

- TBD

## v0.10.0 - App with tests AND coverage AND docs

- TBD

## v0.10.0 - App with Continous Integration

- TBD

## v0.11.0 - App deployed in Heroku

- TBD
