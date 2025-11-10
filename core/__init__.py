# -*- coding: utf-8 -*-
# @Time    : 2025/11/10 下午6:51
# @Author  : fzf
# @FileName: __init__.py
# @Software: PyCharm
__all__ = ['BaseService',
           'BaseVietSet',
           'decorator']

from .base import BaseService,BaseVietSet
from .decorator import decorator as decorator
