# cli-stage
## 中文版
### 项目简介
`cli-stage` 是一个基于 Python 的 CLI 工具框架，结合了 **面向对象的 Service 设计** 与 **Click 命令行工具**，支持：
- 通过 `ViewSet` 类管理所有命令
- 自动将静态方法绑定为 CLI 命令
- 自动调用 Service 的 `handler` 执行具体逻辑
- 支持命令动态注册
- 支持日志和异常捕获
- 可自动生成命令文档（可选）
### 命令说明
| 命令 | 描述 |
|------|------|
| `client` | 客户端相关命令 |
| `readme` | 生成CLI项目的README文档 |

## English Version
### Overview
`cli-stage` is a Python-based CLI tool framework that combines **object-oriented Service design** with **Click command-line tool**, featuring:
- Manage all commands through the `ViewSet` class
- Automatically bind static methods as CLI commands
- Automatically call Service's `handler` to execute logic
- Support dynamic command registration
- Support logging and exception handling
- Optionally generate command documentation automatically
### Command Reference
| Command | Description |
|---------|------------|
| `client` | 客户端相关命令 |
| `readme` | 生成CLI项目的README文档 |
