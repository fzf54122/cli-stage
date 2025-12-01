# -*- coding: utf-8 -*-
# @Time    : 2025/11/24 下午4:01
# @Author  : fzf
# @FileName: ClientService.py
# @Software: PyCharm
import asyncio

from backend.base import BaseService
from backend.core.client import WebSocketClient
from backend.utils.log import get_logger

logger = get_logger(__name__)


class ClientService(BaseService):
    """客户端"""

    async def async_main(*args, **kwargs):
        client = WebSocketClient("ws://127.0.0.1:8000/ws/test/")
        await client.connect()

    def handler(self, *args, **kwargs):
        logger.info(f"[BaseService] 执行客户端逻辑，发送消息:")
        asyncio.get_event_loop().run_until_complete(self.async_main(()))
