# -*- coding: utf-8 -*-
# @Time    : 2025/12/3 下午2:00
# @Author  : fzf
# @FileName: client.py
# @Software: PyCharm
from commons.cli import register_command
from app.utils.decorators import use_service


@register_command('client')
class ClientCommand:
    """客户端命令行"""

    @staticmethod
    @use_service('client')
    def run(service, *args, **kwargs):
        """运行客户端"""
        service.run()
