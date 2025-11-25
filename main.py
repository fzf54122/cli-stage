# -*- coding: utf-8 -*-
# @Time    : 2025/11/10 下午3:05
# @Author  : fzf
# @FileName: main.py
# @Software: PyCharm
import click
from backend import cli as clis
from backend.base import ClickGroup


@click.group(cls=ClickGroup)
def cli():
    pass


if __name__ == "__main__":
    cli()
