# -*- coding: utf-8 -*-
# @Time    : 2025/11/10 下午6:49
# @Author  : fzf
# @FileName: BaseService.py
# @Software: PyCharm
from core import BaseService


class ServerService(BaseService):

    def handler(self, *args, **kwargs):
        print("[BaseService] 启动服务端逻辑...")
        return


class ClientService(BaseService):

    def handler(self, *args, **kwargs):
        print(f"[BaseService] 执行客户端逻辑，发送消息:")
        return



