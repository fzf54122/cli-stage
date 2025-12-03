# -*- coding: utf-8 -*-
# @Time    : 2025/12/3 下午1:58
# @Author  : fzf
# @FileName: decorators.py
# @Software: PyCharm
from functools import wraps
from app.services import ServiceFactory

def use_service(service_name):
    """服务注入装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            service = ServiceFactory.get_service(service_name)
            # 检查是否是实例方法调用（第一个参数是self）
            if args and hasattr(args[0], func.__name__):
                # 实例方法调用：service作为第二个参数传入
                return func(args[0], service, *args[1:], **kwargs)
            else:
                # 普通函数调用：service作为第一个参数传入
                return func(service, *args, **kwargs)
        return wrapper
    return decorator