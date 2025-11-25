# -*- coding: utf-8 -*-
# @Time    : 2025/11/24 下午4:01
# @Author  : fzf
# @FileName: ClientService.py
# @Software: PyCharm
from backend.base import BaseService


class ClientService(BaseService):
    """客户端"""

    def handler(self, *args, **kwargs):
        print(f"[BaseService] 执行客户端逻辑，发送消息:")
        return
