# -*- coding: utf-8 -*-
# @Time    : 2025/12/3 下午1:59
# @Author  : fzf
# @FileName: __init__.py
# @Software: PyCharm


class ServiceFactory:
    """服务工厂类"""
    _services = {}

    @classmethod
    def register(cls, name, service_class):
        """注册服务"""
        cls._services[name] = service_class

    @classmethod
    def get_service(cls, name):
        """获取服务实例"""
        if name not in cls._services:
            # 动态导入服务
            if name == 'client':
                from .client_service import ClientService
                cls.register(name, ClientService)
            elif name == 'server':
                from .server_service import ServerService
                cls.register(name, ServerService)
            elif name == 'readme':
                from .readme_service import ReadmeService
                cls.register(name, ReadmeService)
            else:
                raise ValueError(f"未知服务: {name}")
        # 返回服务实例
        return cls._services[name]()