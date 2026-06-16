# \# inter-agent-collaborative-kit

# \## Introduction

# Lightweight kit for inter-agent communication and collaborative task execution.

# Realize agent registration, cross-agent message interaction, unified task scheduling and joint execution.

# 

# \## 项目简介

# 轻量化跨智能体协同开发套件，标准化实现智能体注册、跨主体消息互通、全局调度、分工协同作业。

# 

# \## Tech Stack

# Python3 | Independent Agent Module | Unified Message Bus

# 

# \### 环境版本硬性要求

# \- Python >= 3.10

# \- Git >= 2.30

# 

# \## 项目目录结构说明

# inter-agent-collaborative-kit/

# ├── .gitignore # Git 过滤配置，不上传缓存、隐私文件

# ├── .env.example # 环境变量模板，本地复制为.env 使用

# ├── requirements.txt # 项目全部 Python 依赖清单

# ├── start.py # 项目统一程序入口

# ├── README.md # 项目说明文档（当前文件）

# ├── agents/ # 全部业务智能体代码

# │ ├── init.py

# │ ├── base\_agent.py # 智能体通用父类

# │ ├── platform\_agent.py # 统筹调度智能体

# │ └── task\_agent.py # 任务执行智能体

# ├── core/ # 框架底层核心逻辑

# │ ├── init.py

# │ ├── message\_bus.py # 跨智能体消息总线（REQ/RPT/SYNC 通信协议）

# │ ├── agent\_manager.py # 智能体注册、生命周期管理

# │ └── task\_dispatch.py # 多智能体任务分发调度

# ├── config/ # 全局配置读取模块

# │ ├── init.py

# │ ├── env.yaml # 运行环境静态参数

# │ ├── agent\_config.yaml # 各智能体专属配置

# │ └── load\_config.py # 统一加载所有配置文件工具

# ├── utils/ # 全局通用工具函数

# │ ├── init.py

# │ ├── logger.py # 统一日志封装

# │ └── common.py # 通用工具、格式转换、时间工具

# ├── tests/ # 单元测试、智能体联调用例

# │ ├── init.py

# │ ├── test\_message\_bus.py # 消息总线单元测试

# │ └── test\_agent\_collab.py # 多智能体协同联调测试

# ├── docs/ # 架构、协议、开发文档

# │ ├── agent\_arch\_v3.md # 多智能体整体架构规范 V3.0

# │ ├── protocol\_spec.md # 智能体消息通信协议详细说明

# │ └── dev\_guide.md # 小组团队开发操作手册

# └── scripts/ # 启停、校验辅助脚本

# ├── start\_collab.bat # Windows 一键启动批处理脚本

# └── verify\_progress.py # 任务进度校验工具脚本

# plaintext

# 

# \## Quick Start 完整部署步骤（Windows CMD）

# \### 1. 克隆项目到本地

# ```bash

# git clone https://github.com/zhu965/inter-agent-collaborative-kit.git

# cd inter-agent-collaborative-kit

# 2\. 创建并激活独立虚拟环境（隔离依赖）

# bash

# 运行

# \# 创建虚拟环境文件夹venv

# python -m venv venv

# 

# \# Windows CMD激活虚拟环境

# venv\\Scripts\\activate

# 激活成功后命令行前缀会出现 (venv) 标识。

# 3\. 一键安装全部项目依赖

# bash

# 运行

# pip install -r requirements.txt

# 4\. 生成本地私有环境配置文件

# 模板文件.env.example仅作参考，本地私有配置.env不会上传 Git

# bash

# 运行

# copy .env.example .env

# 可使用记事本打开.env，修改本地通信端口、日志等级等参数。

# 5\. 启动多智能体协同服务

# 两种启动方式任选其一：

# 方式 1：根目录统一入口启动（推荐开发调试）

# bash

# 运行

# python start.py

# 方式 2：一键批处理脚本启动

# bash

# 运行

# scripts\\start\_collab.bat

# 单元测试运行命令

# 执行所有智能体通信、协同逻辑自动化测试

# bash

# 运行

# pytest tests/ -v

# 团队协作分支管理规范

# main：稳定主干分支，仅存放可正常运行的成品代码，禁止直接在此分支开发、提交代码

# dev-collab：公共开发分支，所有功能开发完成后合并至此

# 新增功能分支命名规则：feat/agent-xxx

# Bug 修复分支命名规则：fix/问题简短描述

# 标准完整开发流程

# 拉取最新公共开发分支代码

# bash

# 运行

# git pull origin dev-collab

# 新建独立功能分支进行开发

# bash

# 运行

# git checkout -b feat/platform-agent-sync

# 编码完成后查看文件变更

# bash

# 运行

# git status

# 提交代码并推送远程仓库

# bash

# 运行

# git add .

# git commit -m "feat: 实现平台智能体同步通信逻辑"

# git push origin feat/platform-agent-sync

# 网页端 GitHub/Gitee 创建合并请求，团队评审后合并至 dev-collab

# Git 提交注释统一规范

# feat: 新增模块、智能体、完整功能

# fix: 修复程序 bug、通信异常、调度错误

# docs: 更新架构文档、协议文档、README

# refactor: 代码重构优化，不改变业务功能

# test: 新增 / 修改单元测试、联调用例

# chore: 调整配置文件、脚本、依赖版本

# 重要注意事项

# .env、venv、模型权重文件夹agent\_weights、日志文件夹logs、缓存文件均已写入.gitignore，不会被提交至远程仓库，保护本地隐私与大文件；

# 智能体通信协议、底层架构详细说明查看docs/目录下 Markdown 文档；

# 任务进度校验工具使用：python scripts/verify\_progress.py;

# 安装新第三方库后，执行以下命令更新依赖清单：

# bash

# 运行

# pip freeze > requirements.txt

# 退出虚拟环境命令：

# bash

# 运行

# deactivate

