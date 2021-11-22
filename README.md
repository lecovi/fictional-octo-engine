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

The run the Flask Development server using `poetry`

```bash
poetry run flask run --host=0.0.0.0
```

### Docker

Build docker image.

```bash
docker build . -t fictional-octo-engine:0.2.0
```

Run the app using `docker` instead of `poetry`.

```bash
docker run --rm --name fictional-octo-engine -v $PWD:/usr/src/app -p 5000:5000 fictional-octo-engine:0.2.0
```