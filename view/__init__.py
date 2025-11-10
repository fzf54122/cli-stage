# -*- coding: utf-8 -*-
# @Time    : 2025/11/10 下午6:24
# @Author  : fzf
# @FileName: view.py
# @Software: PyCharm
__all__ = ['view_set']


from .BaseViewSet import BaseViewSet
view_set = {
    'server': BaseViewSet.server,
    'client': BaseViewSet.client,
    'generate_readme': BaseViewSet.generate_readme,
}
