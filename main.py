# -*- coding: utf-8 -*-
# @Time    : 2025/11/10 下午3:05
# @Author  : fzf
# @FileName: main.py
# @Software: PyCharm
import click

from view import view_set


class ServiceGroup(click.Group):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 初始化时自动注册 ViewSet 中所有方法
        for name, func in view_set.items():
            self.add_command(self.create_command(name, func))

    def create_command(self, name, func):
        @click.command(name, help=func.__doc__)
        def cmd(**kwargs):
            return func()  # 直接调用 ViewSet 的方法

        return cmd


@click.group(cls=ServiceGroup)
def cli():
    pass


if __name__ == "__main__":
    cli()
