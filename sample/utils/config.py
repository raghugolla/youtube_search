from os import environ


def _create_sql_alchemy_url(
    db_url: str, db_user: str, db_pass: str, db_name: str
) -> str:
    return "postgresql+psycopg2://%(user)s:%(pass)s@%(url)s/%(name)s" % {
        "user": db_user,
        "pass": db_pass,
        "name": db_name,
        "url": db_url,
    }


class Config:
    """
    Common configurations
    """

    LOG_LEVEL = environ.get("SAMPLE_LOG_LEVEL", "DEBUG")
    LOG_FORMAT = environ.get("SAMPLE_LOG_FORMAT", "console").lower()
    SQLALCHEMY_ECHO = environ.get("SQLALCHEMY_ECHO", "false") == "true"

    STATSD_API_KEY = environ.get("SAMPLE_STATSD_API_KEY")
    STATSD_APP_KEY = environ.get("SAMPLE_STATSD_APP_KEY")

    db_url = environ.get("SAMPLE_DB_URL")
    db_user = environ.get("SAMPLE_DB_USER")
    db_pass = environ.get("SAMPLE_DB_PASS")
    db_name = environ.get("SAMPLE_DB_NAME")

    SQLALCHEMY_DATABASE_URI = _create_sql_alchemy_url(db_url, db_user, db_pass, db_name)

    EXAPI_SERVICE1_URL = environ.get("SERVICE_ADDR_service1")
    EXAPI_SERVICE2_URL = environ.get("SERVICE_ADDR_service2")

    SQS_QUEUE_PREFIX = environ.get("SQS_QUEUE_PREFIX")
    SQS_REGION = environ.get("SQS_REGION")
    SQS_ENDPOINT_URL = environ.get("SQS_ENDPOINT_URL")

    SENTRY_DSN = environ.get("SENTRY_DSN")
