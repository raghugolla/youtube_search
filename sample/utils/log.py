from .config import Config
from shuttlis.log import configure_logging

LOG = configure_logging("sample", Config.LOG_LEVEL, Config.LOG_FORMAT)
