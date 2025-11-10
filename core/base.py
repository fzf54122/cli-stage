# -*- coding: utf-8 -*-
# @Time    : 2025/11/10 下午6:23
# @Author  : fzf
# @FileName: base.py
# @Software: PyCharm


from abc import ABC, abstractmethod


class BaseService(ABC):

    @abstractmethod
    def handler(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        """直接调用 handler，不用 run"""
        return self.handler(*args, **kwargs)


class BaseVietSet:
    @staticmethod
    def generate_readme(_class, file_path="README.md"):
        """自动生成 CLI 项目的 README 文档（中英文）"""
        # 获取 ViewSet 的所有静态方法
        commands = {
            name: getattr(_class, name)
            for name in dir(_class)
            if callable(getattr(_class, name)) and not name.startswith("__")
        }

        # 中文部分
        zh_lines = [
            "# cli-stage\n",
            "## 中文版\n",
            "### 项目简介\n",
            "`cli-stage` 是一个基于 Python 的 CLI 工具框架，结合了 **面向对象的 Service 设计** 与 **Click 命令行工具**，支持：\n",
            "- 通过 `ViewSet` 类管理所有命令\n",
            "- 自动将静态方法绑定为 CLI 命令\n",
            "- 自动调用 Service 的 `handler` 执行具体逻辑\n",
            "- 支持命令动态注册\n",
            "- 支持日志和异常捕获\n",
            "- 可自动生成命令文档（可选）\n",
            "### 命令说明\n",
            "| 命令 | 描述 |\n",
            "|------|------|\n"
        ]

        # 英文部分
        en_lines = [
            "## English Version\n",
            "### Overview\n",
            "`cli-stage` is a Python-based CLI tool framework that combines **object-oriented Service design** with **Click command-line tool**, featuring:\n",
            "- Manage all commands through the `ViewSet` class\n",
            "- Automatically bind static methods as CLI commands\n",
            "- Automatically call Service's `handler` to execute logic\n",
            "- Support dynamic command registration\n",
            "- Support logging and exception handling\n",
            "- Optionally generate command documentation automatically\n",
            "### Command Reference\n",
            "| Command | Description |\n",
            "|---------|------------|\n"
        ]

        # 遍历命令生成表格
        for name, func in commands.items():
            doc = func.__doc__ or "无描述"
            doc_en = doc  # 英文可以自己改，或从 docstring 中使用英文
            zh_lines.append(f"| `{name}` | {doc} |\n")
            en_lines.append(f"| `{name}` | {doc_en} |\n")

        # 合并内容
        lines = zh_lines + ["\n"] + en_lines

        # 写入文件
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)

        print(f"[INFO] README 已生成: {file_path}")
