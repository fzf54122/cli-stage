# -*- coding: utf-8 -*-
# @Time    : 2025/11/24 下午4:18
# @Author  : fzf
# @FileName: cli.py
# @Software: PyCharm
from backend.base import BaseCli, RegisterCli
from backend.services import use_service


@RegisterCli
class Client(BaseCli):
    """客户端命令行"""

    @use_service('client')
    def run(self, *args, **kwargs):
        pass
