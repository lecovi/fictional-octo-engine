# fictional-octo-engine

A Flask Hello World example

## Prerequisites

This application installs and runs with [poetry](https://python-poetry.org/).
If you don't have it, please follow [Installation Guide](https://python-poetry.org/docs/#installation).

1You also can install it running the following command: `python3 -m pip install poetry --user`

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

Hello, World! from Fictional Octo Engine v0.1.0
```