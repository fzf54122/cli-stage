# -*- coding: utf-8 -*-
# @Time    : 2025/12/3 下午1:57
# @Author  : fzf
# @FileName: main.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
"""CLI-Stage 入口文件"""
# 首先导入所有命令模块，确保装饰器被执行
from app import commands
# 然后创建命令组
from commons.cli import create_click_group
cli = create_click_group()

if __name__ == '__main__':
    cli()