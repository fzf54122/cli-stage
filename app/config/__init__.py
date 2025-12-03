# -*- coding: utf-8 -*-
# @Time    : 2025/12/3 下午1:59
# @Author  : fzf
# @FileName: __init__.py
# @Software: PyCharm
"""配置模块入口"""

from .base import BaseConfig
from .development import DevelopmentConfig

# 根据环境选择配置
config = DevelopmentConfig()
