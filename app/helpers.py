import os
import json
import requests

from .constants import GOOGLE_DISCOVERY_URL


CREDENTIALS_PATH = os.getenv("CREDENTIALS_PATH")


def get_credentials():
    with open(CREDENTIALS_PATH) as creds_file:
        credentials = json.load(creds_file)
    return credentials


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()
