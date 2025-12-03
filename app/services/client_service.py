# -*- coding: utf-8 -*-
# @Time    : 2025/12/3 下午1:58
# @Author  : fzf
# @FileName: client_service.py
# @Software: PyCharm
import asyncio

from app.core.client import WebSocketClient
from app.utils.log import get_logger

logger = get_logger(__name__)

class ClientService:

    async def async_main(*args, **kwargs):
        client = WebSocketClient("ws://127.0.0.1:8000/ws/test/")
        await client.connect()

    def run(self, *args, **kwargs):
        logger.info(f"执行客户端逻辑，发送消息:")
        asyncio.get_event_loop().run_until_complete(self.async_main(()))