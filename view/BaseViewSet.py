# -*- coding: utf-8 -*-
# @Time    : 2025/11/10 下午6:50
# @Author  : fzf
# @FileName: BaseViewSet.py
# @Software: PyCharm

from core import decorator, BaseVietSet as base_view
from services import service_dict

decorator.service_dict = service_dict


class BaseViewSet(base_view):

    @classmethod
    @decorator
    def generate_readme(cls, file_path="README.md"):
        """自动生成 CLI 项目的 README 文档（中英文）"""
        return super().generate_readme(_class=cls, file_path=file_path)

    @staticmethod
    @decorator
    def client():
        """客户端"""

    @staticmethod
    @decorator
    def server():
        """服务端"""
