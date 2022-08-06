# fictional-octo-engine

A Flask Hello World example with Docker.

## Prerequisites

This application installs and runs with [poetry](https://python-poetry.org/).
If you don't have it, please follow [Installation Guide](https://python-poetry.org/docs/#installation).

## Install

```bash
poetry install
```

## Run

Copy environment variables from `env.dist`

```bash
cp env.dist .env
```

Build docker image.

```bash
docker compose build
```

Run the app using `docker-compose` instead of `docker`.

```bash
docker compose up
```

> You can still run the app using `docker run` if you want.

### Running locally

The run the Flask Development server using `poetry`

```bash
poetry run flask run --host=0.0.0.0
```

## Test

Open your browser and go to http://localhost:5000/ and verify that the pages shows
the application name and the current version.

Or use [httpie](https://httpie.io/) in your terminal:

```bash
$ http http://localhost:5000/
HTTP/1.1 200 OK
Connection: close
Content-Length: 47
Content-Type: text/html; charset=utf-8
Date: Sat, 06 Aug 2022 14:35:11 GMT
Server: Werkzeug/2.2.1 Python/3.10.5

Hello, World! from Fictional Octo Engine v0.4.0
```