from flask_keepincheck import HealthCheck
from flask_sqlalchemy import SQLAlchemy

from youtube.utils.flask import APIFlask

db = SQLAlchemy()
healthcheck = HealthCheck()


def configure_db_with_app(app: APIFlask):
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    healthcheck.add_db_check(app=app, db=db)
