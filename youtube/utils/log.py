from .config import Config
from shuttlis.log import configure_logging

LOG = configure_logging("youtube_search", Config.LOG_LEVEL, Config.LOG_FORMAT)
