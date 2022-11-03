import os
import json

from flask import Blueprint, url_for, session, redirect, render_template
from urllib.parse import quote_plus, urlencode

from app.extensions import redis_client, oauth


home = Blueprint('home', __name__)


@home.route('/')
def hello_world():
    name = redis_client.get("app_name").decode()
    version = redis_client.get("app_version").decode()

    return (
        f'Hello, World! from {name} v{version}'
    )


@home.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("home.callback", _external=True)
    )

@home.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/profile")


@home.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + os.getenv("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home.hello_world", _external=True),
                "client_id": os.getenv("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )

@home.route("/profile")
def profile():
    return render_template("profile.html", 
        session=session.get('user'),
        pretty=json.dumps(
            session.get('user'),
            indent=4,
        )
    )
