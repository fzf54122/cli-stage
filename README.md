# 🚀 企业级CLI命令行工具框架

<div align="center">

**一个功能完整、架构清晰的企业级CLI命令行工具框架，支持服务注入和异步通信**

**简体中文** | [English](README.en.md)

<!-- 点赞区域 -->
<div align="center">
  <a href="https://github.com/cli-stage-project" target="_blank">
    <img src="https://img.shields.io/badge/⭐_给个Star-支持项目-FFD700?style=for-the-badge&logo=github&logoColor=white&labelColor=FF6B6B&color=FFD700" alt="给个Star">
  </a>
</div>

<!-- 互动提示 -->
<p align="center">
  ⭐ <strong>喜欢这个项目？点个Star支持一下！</strong> ⭐
</p>

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Click](https://img.shields.io/badge/Click-8.1+-green.svg)](https://click.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![WebSocket](https://img.shields.io/badge/WebSocket-支持-red.svg)](#)
[![Async](https://img.shields.io/badge/异步编程-支持-blue.svg)](#)

[![Architecture](https://img.shields.io/badge/🏗️_架构-命令模式-orange.svg)](#)
[![Dependency Injection](https://img.shields.io/badge/🔧_依赖注入-支持-purple.svg)](#)

[📖 快速开始](#-快速开始) • [🏗️ 架构说明](#-架构说明) • [📚 使用指南](#-使用指南) • [🔧 开发指南](#-开发指南) • [🤝 贡献指南](#-贡献指南) • [🌟 给个Star!](https://github.com/cli-stage-project)

</div>

[//]: # (---)

[//]: # ()
[//]: # (## 📸 项目预览)

[//]: # ()
[//]: # (<div align="center">)

[//]: # ()
[//]: # (### ✨ 核心特性)

[//]: # (<img src="docs/images/features-overview.svg" alt="核心特性" width="700">)

[//]: # ()
[//]: # (### 🛠️ 技术栈)

[//]: # (<img src="docs/images/tech-stack.svg" alt="技术栈" width="700">)

[//]: # ()
[//]: # (</div>)

[//]: # ()
[//]: # (---)

## 🌟 为什么选择这个CLI框架？

<div align="center">

| 🎯 **命令模式** | ⚡ **服务注入** | 🛡️ **异步支持** | 📈 **扩展性强** |
|:---:|:---:|:---:|:---:|
| 基于Click的命令行接口<br/>优雅的命令注册机制 | 灵活的依赖注入<br/>服务自动管理 | 完整异步支持<br/>WebSocket通信 | 模块化设计<br/>易于扩展新命令 |

</div>

## ✨ 核心特性

### 🔧 命令行功能
- **命令注册装饰器** - 简单易用的`@register_command`装饰器，一键注册命令
- **命令分组** - 支持多级命令分组，清晰的命令层次结构
- **参数解析** - 基于Click的强大参数处理能力，支持各种参数类型
- **帮助文档** - 自动生成详细的命令帮助文档

### 📦 服务管理
- **服务注入** - 优雅的`@use_service`装饰器，自动注入所需服务
- **服务工厂** - 统一的服务注册和获取机制
- **依赖管理** - 服务依赖的自动解析和管理
- **单例模式** - 服务实例的统一管理

### 🌐 异步通信
- **WebSocket支持** - 内置WebSocket客户端实现
- **异步命令** - 支持异步命令处理
- **事件循环管理** - 自动处理事件循环的创建和销毁
- **并发处理** - 高效的并发命令执行

### 🏗️ 架构设计
- **命令模式** - 清晰的命令对象设计
- **依赖注入** - 松耦合的组件设计
- **模块化结构** - 清晰的代码组织结构
- **类型安全** - 完整的Python类型注解

## 🛠️ 技术栈

| 组件 | 技术选型 | 版本要求 |
|------|----------|----------|
| **语言** | Python | 3.11+ |
| **CLI框架** | Click | 8.1+ |
| **异步支持** | asyncio | 内置 |
| **WebSocket** | websockets | 11.0+ |
| **配置管理** | pydantic | 2.0+ |
| **类型检查** | mypy | 1.5+ |
| **日志** | logging | 内置 |

## 📁 项目结构

```
cli-stage/
├── main.py                       # 🚀 主入口文件
├── app/                          # 📦 应用代码目录
│   ├── commands/                 # 🎯 命令实现
│   │   ├── client.py             # 👥 客户端命令
│   │   └── __init__.py           # 📋 命令初始化
│   ├── services/                 # 🔧 服务层
│   │   ├── client_service.py     # 🌐 客户端服务
│   │   └── __init__.py           # 📋 服务初始化
│   ├── core/                     # ⚙️ 核心功能
│   │   ├── client/               # 👥 客户端核心
│   │   │   └── __init__.py       # 📋 客户端初始化
│   │   └── __init__.py           # 📋 核心初始化
│   ├── config/                   # 🔧 配置管理
│   │   ├── __init__.py           # 📋 配置初始化
│   │   ├── base.py               # 📝 基础配置
│   │   └── development.py        # 🧪 开发配置
│   └── utils/                    # 🛠️ 工具函数
│       └── decorators.py         # 🔧 装饰器实现
├── commons/                      # 📚 通用组件
│   └── cli/                      # 🎯 CLI通用组件
│       └── group.py              # 👥 命令组实现
├── pyproject.toml                # 📦 项目配置
├── requirements.txt              # 📋 依赖列表
└── README.md                     # 📚 项目说明
```

## 🚀 快速开始

### ⚡ 安装依赖

```bash
# 克隆项目
git clone <your-repo-url>
cd cli-stage

# 安装依赖
pip install -r requirements.txt
```

### 💻 基本使用

```bash
# 查看帮助信息
python main.py --help

# 运行客户端命令
python main.py client
```

## 📚 使用指南

### 基础命令

```bash
# 查看版本信息
python main.py --version

# 查看所有可用命令
python main.py --help

# 查看特定命令的帮助
python main.py client --help
```

### 客户端命令

客户端命令用于建立WebSocket连接并进行通信：

```bash
# 运行客户端
python main.py client

# 带参数运行客户端
python main.py client --host localhost --port 8765
```

## 🏗️ 架构说明

### 命令注册机制

命令通过装饰器方式注册到命令组：

```python
from commons.cli.group import register_command

@register_command('client')
class ClientCommand:
    def run(self, service, *args, **kwargs):
        # 命令实现
        service.run()
```

### 服务注入机制

通过装饰器自动注入所需服务：

```python
from app.utils.decorators import use_service

class ClientCommand:
    @use_service('client')
    def run(self, service, *args, **kwargs):
        # service 已自动注入为 ClientService 实例
        service.run()
```

### WebSocket通信

客户端服务支持异步WebSocket通信：

```python
import asyncio
from websockets.asyncio.client import connect

class WebSocketClient:
    async def connect(self, uri):
        # WebSocket连接逻辑
        pass
```

## 🔧 开发指南

### 添加新命令

1. 在 `app/commands/` 目录下创建新的命令文件
2. 定义命令类并使用 `@register_command` 装饰器
3. 实现 `run` 方法处理命令逻辑

```python
# app/commands/my_command.py
from commons.cli.group import register_command
from app.utils.decorators import use_service

@register_command('mycommand')
class MyCommand:
    @use_service('myservice')
    def run(self, service, *args, **kwargs):
        # 命令实现
        service.do_something()
```

### 添加新服务

1. 在 `app/services/` 目录下创建新的服务文件
2. 定义服务类并实现所需功能
3. 在 `app/services/__init__.py` 中注册服务

```python
# app/services/my_service.py
class MyService:
    def do_something(self):
        # 服务实现
        print("Service doing something...")
```

## 🎯 路线图

- [x] ✅ **v1.0** - 基础命令行框架和服务注入
- [x] ✅ **v1.1** - WebSocket客户端支持
- [x] ✅ **v1.2** - 异步命令处理
- [ ] 🚧 **v1.3** - 配置文件支持
- [ ] 📅 **v1.4** - 插件系统
- [ ] 📅 **v1.5** - 命令自动补全
- [ ] 📅 **v2.0** - GUI界面支持

---

## 🤝 贡献指南

欢迎各位开发者参与项目贡献！贡献方式包括：

1. **Bug报告** - 通过GitHub Issues提交Bug报告
2. **功能请求** - 提出新功能或改进建议
3. **代码贡献** - 提交Pull Request改进代码
4. **文档完善** - 帮助完善项目文档

## 📄 许可证

本项目采用MIT许可证 - 详情请查看 [LICENSE](LICENSE) 文件

---

## 💖 鸣谢

感谢所有支持和贡献这个项目的开发者！

- 特别感谢 [Click](https://click.palletsprojects.com/) 提供优秀的命令行框架
- 感谢 [websockets](https://websockets.readthedocs.io/) 提供异步WebSocket支持
- 感谢所有使用和反馈的用户！

---

> 💡 **提示**：本框架设计为轻量级但功能强大的命令行工具开发基础，适用于各种CLI应用场景。
> 
> 🚀 **开始使用**：按照快速开始指南，5分钟内即可启动您的CLI项目！