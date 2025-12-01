# -*- coding: utf-8 -*-
# @Time    : 2025/11/28 下午5:00
# @Author  : fzf
# @FileName: app.py
# @Software: PyCharm
import asyncio
import json

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from .manage import manager
from backend.utils.log import get_logger

logger = get_logger(__name__)
app = FastAPI()


@app.on_event("startup")
async def startup_event():
    # 启动 Redis 监听后台任务
    asyncio.create_task(manager.redis_listener())


@app.websocket("/ws/{group}/")
async def websocket_endpoint(websocket: WebSocket, group: str):
    """WebSocket 接口，客户端传入分组参数"""
    await websocket.accept()  # 先接受
    await manager.connect(websocket, group)

    try:
        while True:
            # 等待客户端发送消息
            data = await websocket.receive_text()
            decoded = json.loads(data)
            logger.info(f"[WS] 收到消息来自组 {group}: {decoded.get('msg')}")
            # 回显给组内其他客户端
            await manager.send_group(group, f"来自组 {group} 的广播: {decoded.get('msg')}")
    except WebSocketDisconnect:
        manager.disconnect(websocket, group)
