# -*- coding: utf-8 -*-
# @Time    : 2025/12/3 下午2:00
# @Author  : fzf
# @FileName: readme.py
# @Software: PyCharm
from commons.cli import register_command
from app.utils.decorators import use_service


@register_command('readme')
class ReadmeCommand:
    """生成CLI项目的README文档"""

    @staticmethod
    @use_service('readme')
    def run(service, *args, **kwargs):
        """自动生成 CLI 项目的 README 文档（中英文）"""
        service.run()
