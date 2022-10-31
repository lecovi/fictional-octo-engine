from flask import current_app
from flask.cli import AppGroup

from app.extensions import db


db_cli = AppGroup('db')


@db_cli.command("init", help="Initialize Database Schema")
def init_db():
    db.create_all()
    current_app.logger.info("Creating DB...")


@db_cli.command("drop", help="Drops Database Schema")
def drop_db():
    db.drop_all()
    current_app.logger.info("Dropping DB...")
