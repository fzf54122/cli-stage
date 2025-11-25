import logging
from backend.settings import settings
from rich.logging import RichHandler

default_level = logging.INFO if not settings.debug else logging.DEBUG


def get_logger(name, level=default_level):
    return _get_rich_logger(name, level)


def _get_standard_logger(name, level=default_level):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    FORMAT = "[%(asctime)s][%(levelname)s][%(filename)s][line %(lineno)s][%(funcName)5s()]: %(message)s"
    formatter = logging.Formatter(FORMAT)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


def _get_rich_logger(name, level=default_level):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    FORMAT = "[%(filename)s][line %(lineno)s][%(funcName)5s()]: %(message)s"
    formatter = logging.Formatter(FORMAT)
    console_handler = RichHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger