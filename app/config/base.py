# -*- coding: utf-8 -*-
# @Time    : 2025/12/3 下午2:00
# @Author  : fzf
# @FileName: base.py
# @Software: PyCharm
"""基础配置模块"""


class BaseConfig:
    """基础配置类"""
    DEBUG = False
    CLI_COMMANDS = {}

    @classmethod
    def register_command(cls, name, command_class):
        """注册命令"""
        # print(f"注册命令: {name} -> {command_class.__name__}")
        cls.CLI_COMMANDS[name] = command_class
        # print(f"当前注册的命令: {list(cls.CLI_COMMANDS.keys())}")