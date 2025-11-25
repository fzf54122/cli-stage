# -*- coding: utf-8 -*-
# @Time    : 2025/11/24 下午3:51
# @Author  : fzf
# @FileName: service.py
# @Software: PyCharm
import click
from abc import ABC, abstractmethod


class BaseService(ABC):

    @abstractmethod
    def handler(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        """直接调用 handler，不用 run"""
        return self.handler(*args, **kwargs)
