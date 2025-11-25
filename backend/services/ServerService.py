# -*- coding: utf-8 -*-
# @Time    : 2025/11/24 下午4:01
# @Author  : fzf
# @FileName: ServerService.py
# @Software: PyCharm
from backend.base import BaseService


class ServeService(BaseService):
    """服务端"""

    def handler(self, *args, **kwargs):
        print("[BaseService] 启动服务端逻辑...")
        return
