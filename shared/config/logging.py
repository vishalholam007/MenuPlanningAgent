from loguru import logger
import sys
import os

os.makedirs("logs", exist_ok=True)

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True
)

logger.add(
    "logs/application.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO"
)

logger.add(
    "logs/error.log",
    rotation="10 MB",
    retention="30 days",
    level="ERROR"
)