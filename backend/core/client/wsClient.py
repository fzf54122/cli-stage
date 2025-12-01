# -*- coding: utf-8 -*-
# @Time    : 2025/11/28 下午5:05
# @Author  : fzf
# @FileName: wsClint.py
# @Software: PyCharm
# ws_client_cli.py
import asyncio
import websockets
import json
from backend.utils.log import get_logger

logger = get_logger(__name__)

class WebSocketClient:
    def __init__(self, url: str):
        self.url = url
        self.connection = None
        self.listen_task = None

    async def connect(self):
        logger.info(f"连接 WebSocket: {self.url}")
        self.connection = await websockets.connect(self.url)
        # 后台监听服务端消息
        self.listen_task = asyncio.create_task(self.listen())
        # 等待监听任务结束（实际上是无限监听）
        await self.listen_task

    async def listen(self):
        """后台监听服务端消息"""
        try:
            async for message in self.connection:
                try:
                    data = json.loads(message)
                except:
                    data = message
                logger.info(f"[收到] {data}")
        except websockets.ConnectionClosed:
            logger.warning("WebSocket 已关闭")
        except Exception as e:
            logger.error(f"监听错误: {e}")

    async def close(self):
        """关闭连接"""
        if self.connection:
            await self.connection.close()
            logger.info("WebSocket 已关闭")
        if self.listen_task:
            self.listen_task.cancel()

# 启动示例
if __name__ == "__main__":
    client = WebSocketClient("ws://127.0.0.1:8000/ws/test")
    asyncio.run(client.connect())
