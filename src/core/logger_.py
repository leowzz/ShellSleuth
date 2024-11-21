import sys

from loguru import logger

from src.core.config import setting


def init_logger():
    logger.remove()
    if setting.debug:
        logger.add(sys.stderr, level="DEBUG")
    else:
        logger.add(sys.stderr, level="INFO")
