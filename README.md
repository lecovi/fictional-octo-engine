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
docker-compose build
```

Run the app using `docker-compose` instead of `docker`.

```bash
docker-compose up
```

> You can still run the app using `docker run` if you want.

### Running locally

The run the Flask Development server using `poetry`

```bash
poetry run flask run --host=0.0.0.0
```