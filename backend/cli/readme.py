# -*- coding: utf-8 -*-
# @Time    : 2025/11/24 下午4:20
# @Author  : fzf
# @FileName: generate_readme.py
# @Software: PyCharm
from backend.base import BaseCli, RegisterCli
from backend.services import use_service


@RegisterCli
class Readme(BaseCli):
    """生成CLI项目的README文档"""

    @use_service('readme')
    def run(self, *args, **kwargs):
        pass
