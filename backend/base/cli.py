# -*- coding: utf-8 -*-
# @Time    : 2025/11/24 下午4:54
# @Author  : fzf
# @FileName: cli.py
# @Software: PyCharm
from abc import ABC, abstractmethod


class BaseCli(ABC):

    def run(self, *args, **kwargs):
        """启动服务"""
        pass
