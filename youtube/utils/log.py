from shuttlis.log import configure_logging

from .config import Config

LOG = configure_logging("youtube", Config.LOG_LEVEL, Config.LOG_FORMAT)
