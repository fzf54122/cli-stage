# -*- coding: utf-8 -*-
# @Time    : 2025/12/3 下午1:58
# @Author  : fzf
# @FileName: server_service.py
# @Software: PyCharm
import uvicorn

from app.core.server import app
from app.utils.log import get_logger

logger = get_logger(__name__)


class ServerService:

    def run(self, *args, **kwargs):
        logger.info("启动服务端逻辑...")
        uvicorn.run(app, host="127.0.0.1", port=8000, log_level='error')
