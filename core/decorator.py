# -*- coding: utf-8 -*-
# @Time    : 2025/11/10 下午3:00
# @Author  : fzf
# @FileName: utils.py
# @Software: PyCharm
import functools

from .base import BaseService

from services import service_dict


class ServiceDecorator:

    def __init__(self, action=None):
        self.action = action
        self.service_dict = service_dict

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            method_name = func.__name__
            action = self.action or method_name
            service_func = service_dict.get(action, None)
            try:
                if service_func and issubclass(service_func, BaseService):
                    print(f"[Service] 调用 CLI 方法: {service_func.__name__}, action={action}")
                    service_instance = service_func()
                    return service_instance(*args, **kwargs)
                else:
                    print(f"[Service] 未找到 service 对应 action: {action}, 执行原函数")
                    return func(*args, **kwargs)
            except Exception as e:
                print(f"[Service] 执行 {action} 出错: {e}")
                return None

        return wrapper


decorator = ServiceDecorator()
