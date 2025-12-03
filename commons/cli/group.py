# -*- coding: utf-8 -*-
# @Time    : 2025/12/3 下午2:08
# @Author  : fzf
# @FileName: group.py
# @Software: PyCharm
"""Click 命令组"""

import click
import functools


def create_click_group():
    """创建命令组"""
    # 使用局部导入避免循环依赖
    from app.config import config

    @click.group()
    def cli():
        """CLI-Stage 命令行工具"""
        pass

    # 动态注册所有命令
    for cmd_name, cmd_class in config.CLI_COMMANDS.items():
        _register_command_to_group(cli, cmd_name, cmd_class)

    return cli


def _register_command_to_group(cli_group, name, command_class):
    """将命令注册到命令组"""
    # 创建命令实例
    instance = command_class()

    # 创建命令组
    @cli_group.group(name=name, help=command_class.__doc__)
    def sub_cmd():
        pass


    # 注册实例方法作为子命令
    for attr_name in dir(instance):
        if attr_name.startswith('_'):
            continue
        method = getattr(instance, attr_name)
        if callable(method) and not isinstance(method, type):
            # 修复：正确处理装饰器装饰的实例方法
            # 创建子命令时，直接使用已装饰的方法
            @click.command(name=attr_name, help=method.__doc__ or '')
            @functools.wraps(method)
            def wrapper(*args, **kwargs):
                # 直接调用已装饰的方法，装饰器会自动处理服务注入
                return method(*args, **kwargs)

            # 添加到命令组
            sub_cmd.add_command(wrapper)
