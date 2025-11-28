# -*- coding: utf-8 -*-
# @Time    : 2025/11/24 下午4:01
# @Author  : fzf
# @FileName: ServerService.py
# @Software: PyCharm
from backend.base import BaseService
from backend.utils.log import get_logger

logger = get_logger(__name__)


class ServeService(BaseService):
    """服务端"""

    def handler(self, *args, **kwargs):
        logger.info("启动服务端逻辑...")
        return
