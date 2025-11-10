# -*- coding: utf-8 -*-
# @Time    : 2025/11/10 下午6:24
# @Author  : fzf
# @FileName: service.py
# @Software: PyCharm
__all__ = ['service_dict']

from .BaseService import ServerService, ClientService

service_dict = {
    'server': ServerService,
    'client': ClientService,
}
