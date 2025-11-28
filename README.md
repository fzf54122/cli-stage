# CLI-Stage

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Click-7.0%2B-green.svg" alt="Click Version">
  <img src="https://img.shields.io/badge/Rich-10.0%2B-yellow.svg" alt="Rich Version">
  <img src="https://img.shields.io/badge/Architecture-OOP-orange.svg" alt="Architecture">
</div>

## 项目简介

**CLI-Stage** 是一个优雅的 Python CLI 工具框架，融合了面向对象设计与命令行交互的最佳实践。它提供了一套完整的命令注册、服务注入和执行流程，使开发者能够快速构建功能丰富、结构清晰的命令行应用程序。

### 核心特性

- **自动命令注册**：通过装饰器自动将类方法注册为 CLI 命令
- **依赖注入**：优雅的服务注入机制，实现业务逻辑与命令接口的解耦
- **面向对象**：基于类的命令和服务设计，符合 Python 最佳实践
- **自动文档**：自动生成命令帮助信息和项目 README 文档
- **统一日志**：集成 Rich 日志美化，提供友好的日志输出体验
- **异常处理**：标准化的异常处理流程，提升应用健壮性

## 架构设计

CLI-Stage 采用分层架构设计，将命令定义与业务逻辑分离，实现高度的模块化和可扩展性。

### 架构图

```mermaid
flowchart LR

A[main.py<br>命令入口] --> B[Click Group<br>命令集合]
B --> C[RegisterCli<br>自动发现命令]
C --> D[BaseCli 子类<br>定义业务命令]
D --> E[依赖注入<br>@use_service]
E --> F[ServiceFactory<br>创建服务实例]
F --> G[BaseService 子类<br>执行业务逻辑]
```
### 核心组件

- **BaseCli**：所有命令类的抽象基类，提供统一的接口
- **BaseService**：所有服务类的抽象基类，定义业务逻辑的标准接口
- **ClickGroup**：增强的 Click 命令组，支持命令动态注册
- **RegisterCli**：命令注册装饰器，自动将类方法注册为 CLI 命令
- **ServiceFactory**：服务工厂，负责创建和管理服务实例
- **use_service**：服务注入装饰器，实现命令与服务的解耦

## 快速开始

### 环境要求

- Python 3.8+
- Click 7.0+
- Rich 10.0+

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行命令

```bash
python main.py --help
```

## 命令参考

### 命令概览

| 命令    | 描述                  |
|---------|-----------------------|
| client  | 客户端相关操作        |
| serve   | 服务端相关操作        |
| readme  | 生成项目 README 文档  |

### 详细命令说明

#### client 命令

客户端操作命令，用于管理客户端相关功能。

```bash
python main.py client
```

#### serve 命令

服务端操作命令，用于管理服务端相关功能。

```bash
python main.py serve
```

#### readme 命令

自动生成项目的 README 文档，包含中英文版本。

```bash
python main.py readme
```

## 扩展指南

### 添加新命令

要添加新的 CLI 命令，请按照以下步骤操作：

1. 在 `backend/cli/` 目录下创建新的命令文件
2. 创建继承自 `BaseCli` 的命令类
3. 使用 `@RegisterCli` 装饰器注册命令
4. 使用 `@use_service` 装饰器绑定服务
5. 在 `backend/services/` 目录下创建对应的服务类
6. 在 `services/__init__.py` 中注册新服务

示例：

```python
# backend/cli/mycommand.py
from backend.base import BaseCli, RegisterCli
from backend.services import use_service

@RegisterCli
class MyCommand(BaseCli):
    """我的自定义命令"""
    
    @use_service('myservice')
    def run(self, *args, **kwargs):
        pass
```

### 自定义日志

CLI-Stage 集成了 Rich 日志库，可以通过 `backend.utils.log` 中的函数使用增强的日志功能：

```python
from backend.utils.log import get_logger

logger = get_logger(__name__)
logger.info("这是一条信息日志")
logger.warning("这是一条警告日志")
logger.error("这是一条错误日志")
```

## 最佳实践

- **命令与服务分离**：将命令定义与业务逻辑分离，提高代码可维护性
- **使用装饰器**：充分利用 `@RegisterCli` 和 `@use_service` 装饰器简化代码
- **标准化错误处理**：在服务类中统一处理异常，保持命令接口简洁
- **完善文档**：为命令和服务添加详细的文档字符串，便于自动生成文档

## 贡献指南

欢迎贡献代码！请遵循以下规范：

1. Fork 项目仓库
2. 创建功能分支
3. 提交代码更改
4. 运行测试
5. 提交 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详见 LICENSE 文件

---

<p align="center">Made with ❤️ by CLI-Stage Team</p>