# -*- coding: utf-8 -*-
# @Time    : 2025/11/24 下午3:51
# @Author  : fzf
# @FileName: __init__.py
# @Software: PyCharm
__all__ = [
    'BaseCli',
    'BaseService',
    "ClickGroup",
    'RegisterCli'

]
from .cli import BaseCli
from .service import BaseService
from .cli_group import RegisterCli,ClickGroup
