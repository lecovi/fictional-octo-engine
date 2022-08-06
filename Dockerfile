FROM python:3.10-alpine

# Install curl and dependencies needed for poetry
RUN apk add --update curl
RUN apk add --update g++
RUN rm -rf /var/cache/apk/*

# Upgrades pip
RUN python -m pip install --upgrade pip

# Installs poetry
RUN curl -sSL \
    https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | \
    python -
ENV PATH /root/.poetry/bin:$PATH

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
