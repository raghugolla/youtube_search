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

    LOG_LEVEL = environ.get("YOUTUBE_LOG_LEVEL", "DEBUG")
    LOG_FORMAT = environ.get("YOUTUBE_LOG_FORMAT", "console").lower()
    SQLALCHEMY_ECHO = environ.get("SQLALCHEMY_ECHO", "false") == "true"

    db_url = environ.get("YOUTUBE_DB_URL")
    db_user = environ.get("YOUTUBE_DB_USER")
    db_pass = environ.get("YOUTUBE_DB_PASS")
    db_name = environ.get("YOUTUBE_DB_NAME")

    SQLALCHEMY_DATABASE_URI = _create_sql_alchemy_url(db_url, db_user, db_pass, db_name)

    YOUTUBE_URL = environ.get("YOUTUBE_URL", "https://youtube.googleapis.com")

    API_KEY = environ.get("API_KEY", "AIzaSyDkuSGzpTDkv--dJ8odnkQ2j9l8fqxO3cE")
