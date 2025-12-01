# -*- coding: utf-8 -*-
# @Time    : 2025/11/28 下午5:00
# @Author  : fzf
# @FileName: manage.py
# @Software: PyCharm
from fastapi import WebSocket, WebSocketDisconnect
from typing import Dict, List
from backend.utils.log import get_logger

import aioredis

logger = get_logger(__name__)
class WebSocketManager:
    """WebSocket 连接管理器，支持分组"""
    def __init__(self):
        self.connections: Dict[str, List[WebSocket]] = {}  # 分组管理

    async def connect(self, websocket: WebSocket, group: str):
        """客户端连接，加入分组"""
        self.connections.setdefault(group, []).append(websocket)
        logger.info(f"[WS] 新连接加入组 {group}，当前组数量：{len(self.connections[group])}")

    def disconnect(self, websocket: WebSocket, group: str):
        """客户端断开，移出分组"""
        if group in self.connections:
            self.connections[group].remove(websocket)
            if not self.connections[group]:
                del self.connections[group]
            logger.info(f"[WS] 断开连接，组 {group} 当前数量：{len(self.connections.get(group, []))}")

    async def send_group(self, group: str, message: str):
        """发送消息到分组内所有客户端"""
        if group in self.connections:
            for ws in list(self.connections[group]):
                try:
                    await ws.send_text(message)
                except WebSocketDisconnect:
                    self.disconnect(ws, group)

    async def redis_listener(self):
        redis = await aioredis.from_url("redis://localhost", db=10)
        pubsub = redis.pubsub()

        groups = ["test", "vip"]
        for g in groups:
            await pubsub.subscribe(f"group:{g}")

        logger.info("Redis 监听启动...")
        async for message in pubsub.listen():
            if message["type"] == "message":
                data = message["data"]
                channel = message["channel"]
                if isinstance(data, bytes):
                    data = data.decode()
                if isinstance(channel, bytes):
                    channel = channel.decode()
                group = channel.split(":")[1]
                logger.info(f"[Redis] 收到消息 {data} -> group {group}")
                await self.send_group(group, f"[Redis推送] {data}")

manager = WebSocketManager()
