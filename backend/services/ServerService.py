# -*- coding: utf-8 -*-
# @Time    : 2025/11/24 下午4:01
# @Author  : fzf
# @FileName: ServerService.py
# @Software: PyCharm
import uvicorn
from backend.base import BaseService
from backend.utils.log import get_logger
from backend.core.serve import app

logger = get_logger(__name__)


class ServeService(BaseService):
    """服务端"""

    def handler(self, *args, **kwargs):
        logger.info("启动服务端逻辑...")
        uvicorn.run(app, host="127.0.0.1", port=8000)
        return True
