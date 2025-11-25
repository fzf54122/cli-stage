# -*- coding: utf-8 -*-
# @Time    : 2025/11/24 下午4:20
# @Author  : fzf
# @FileName: serve.py
# @Software: PyCharm
from backend.base import BaseCli, RegisterCli
from backend.services import use_service


@RegisterCli
class Serve(BaseCli):
    """服务端命令行"""

    @use_service('serve')
    def run(self, *args, **kwargs):
        pass
