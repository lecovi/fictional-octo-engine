# fuzzy-lamp
A Flask Hello World example

## Prerequisites

This application installs and runs with [poetry](https://python-poetry.org/).
If you don't have it, please follow [Installation Guide](https://python-poetry.org/docs/#installation).
You also can install it running the following command: `python3 -m pip install poetry --user`

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
