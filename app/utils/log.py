# -*- coding: utf-8 -*-
# @Time    : 2025/12/3 下午4:04
# @Author  : fzf
# @FileName: log.py
# @Software: PyCharm
import logging
from rich.logging import RichHandler
from app.config import config

default_level = logging.INFO if not config.DEBUG else logging.DEBUG


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