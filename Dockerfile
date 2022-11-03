FROM python:3.10-alpine

# Install curl and dependencies needed for poetry
RUN apk add --update curl
RUN apk add --update g++
RUN apk add --update libffi-dev
RUN rm -rf /var/cache/apk/*

# Upgrades pip
RUN python -m pip install --upgrade pip

# Installs poetry
ENV POETRY_HOME /opt/poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH $POETRY_HOME/bin:$PATH

WORKDIR /usr/src/app
COPY pyproject.toml .
# Create poetry venv and updates pip inside it
RUN poetry run python -m pip install --upgrade pip
# Install app deps
COPY poetry.lock .
RUN poetry install

# Copy code
COPY . .

# Run application
CMD poetry run flask run --host=0.0.0.0
