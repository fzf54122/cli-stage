# -*- coding: utf-8 -*-
# @Time    : 2025/11/10 下午6:24
# @Author  : fzf
# @FileName: service.py
# @Software: PyCharm
__all__ = ['ClientService',
           'ReadmeService',
           'ServerService',
           'use_service', ]

from .ClientService import ClientService
from .ServerService import ServeService
from .ReadmeService import ReadmeService


class ServiceFactory:
    """根据名称获取 Service 实例"""
    service_mapping = {
        "client": ClientService,
        "serve": ServeService,
        "readme": ReadmeService,
    }

    @classmethod
    def set_service(cls, name: str):
        service_cls = cls.service_mapping.get(name.lower())
        if not service_cls:
            raise ValueError(f"Service {name} 不存在")
        return service_cls()


def use_service(name):
    """将对应的 Service 实例注入到函数"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            service = ServiceFactory.set_service(name)
            service.handler(*args, **kwargs)
            return func(service, *args, **kwargs)

        return wrapper

    return decorator
