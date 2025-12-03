# -*- coding: utf-8 -*-
# @Time    : 2025/12/3 下午2:00
# @Author  : fzf
# @FileName: server.py
# @Software: PyCharm
from commons.cli import register_command
from app.utils.decorators import use_service


@register_command('server')
class ServerCommand:
    """服务端命令行"""

    @staticmethod
    @use_service('server')
    def run(service, *args, **kwargs):
        """启动服务端"""
        service.run()