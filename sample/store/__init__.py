from flask_sqlalchemy import SQLAlchemy
from sample.utils.flask import APIFlask
from flask_keepincheck import HealthCheck

db = SQLAlchemy()
healthcheck = HealthCheck()


def configure_db_with_app(app: APIFlask):
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    healthcheck.add_db_check(app=app, db=db)
