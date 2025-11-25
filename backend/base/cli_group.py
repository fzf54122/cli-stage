# -*- coding: utf-8 -*-
# @Time    : 2025/11/24 下午4:04
# @Author  : fzf
# @FileName: clickGroup.py
# @Software: PyCharm
import functools

import click
from backend.utils.log import get_logger

logger = get_logger(__name__)

view_set = {}


def RegisterCli(cls):
    """自动扫描类中的实例方法，并注册到 view_cli"""
    view_set[cls.__name__.lower()] = cls
    return cls


class ClickGroup(click.Group):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 遍历 view_set，把类注册成一级 group
        for cls_name, cls in view_set.items():
            # 一级命令的 help 来自类 docstring
            grp = click.Group(name=cls_name, help=cls.__doc__)
            instance = cls()

            for attr_name in dir(instance):
                if attr_name.startswith("_"):
                    continue
                method = getattr(instance, attr_name)
                if callable(method):
                    # 子命令的 help 来自方法 docstring
                    grp.add_command(self.create_command(attr_name, method))

            self.add_command(grp)

    def create_command(self, name, func):
        @click.command(name=name, help=func.__doc__)
        @functools.wraps(func)
        def cmd(**kwargs):
            return func()

        return cmd
