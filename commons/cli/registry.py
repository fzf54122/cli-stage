# -*- coding: utf-8 -*-
# @Time    : 2025/12/3 下午2:08
# @Author  : fzf
# @FileName: registry.py
# @Software: PyCharm

"""命令注册器"""

import functools

def register_command(name=None):
    """命令注册装饰器"""
    def decorator(cls):
        # 使用局部导入避免循环依赖
        from app.config import config
        command_name = name or cls.__name__.lower().replace('command', '')
        config.register_command(command_name, cls)
        return cls
    return decorator