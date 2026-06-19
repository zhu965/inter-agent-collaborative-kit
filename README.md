# INTER-AGENT-COLLABORATIVE-KIT
OpenClaw v5.2 联邦式多智能体协同开发框架

## 一、项目概述
### 1. 项目定位
一套轻量化、可分布式部署的多智能体协作底层框架，面向多角色业务Agent协同通信场景。
框架内置统一MQTT消息总线、安全签名校验、合规管控、分层文件存储、路由权限过滤能力，无需从零封装通信与安全能力，开箱即用。

### 2. 核心能力
1. **分布式消息总线**：基于EMQX MQTT实现点对点单播、全局广播两种消息分发模式；
2. **全链路安全机制**：ECDSA非对称签名验签、TLS加密传输（生产环境），防止消息篡改、伪造；
3. **全局合规管控**：内置合规阈值校验，违规行为统一告警上报至管控智能体；
4. **分层存储隔离**：不同角色智能体数据独立目录存储，避免文件混乱；
5. **模块化Agent设计**：统一基类抽象，新增业务智能体仅需继承基类、注册消息回调即可；
6. **环境隔离**：通过.env文件区分开发/局域网/线上多套环境配置。

### 3. 六大内置业务智能体职责
| 智能体名称 | 核心定位 | 主要职责 |
| ---- | ---- | ---- |
| ArchAgent 架构智能体 | 全局调度核心 | MQTT总线初始化、存储目录管理、全系统事件转发、服务状态监控 |
| CeoAgent 管控智能体 | 安全合规中心 | 合规阈值校验、异常告警接收、全局权限黑白名单管控、审计日志汇总 |
| PmAgent 项目智能体 | 业务流程调度 | 项目任务分发、多智能体任务同步、业务流程状态流转管理 |
| AlgorithmAgent 算法智能体 | 数据计算节点 | 数据集接收存储、模型训练任务处理、算法结果回传上报 |
| PlatformAgent 平台智能体 | 资源运维节点 | 服务器资源监控、存储配额校验、服务启停管理 |
| MarketAgent 市场智能体 | 业务数据节点 | 业务统计、市场报表生成、业务数据汇总上报 |

## 二、完整目录结构
```
inter-agent-collaborative-kit/
├── agents/                          # 所有业务智能体模块
│   ├── base_federate_agent.py       # Agent统一基类（封装总线、存储、合规通用逻辑）
│   ├── __init__.py                  # Python包导出标识
│   ├── arch/                        # 架构智能体代码
│   │   ├── arch_main.py
│   │   └── __init__.py
│   ├── ceo/                         # 管控智能体代码
│   ├── pm/                          # 项目智能体代码
│   ├── algorithm/                   # 算法智能体代码
│   ├── platform/                    # 平台智能体代码
│   └── market/                      # 市场业务智能体代码
├── core/                            # 底层核心公共工具包
│   ├── __init__.py
│   ├── federate_bus.py              # MQTT消息总线封装（单播/广播、连接管理）
│   ├── compliance_checker.py        # 合规阈值校验工具
│   ├── message_builder.py           # 标准化消息结构体生成工具
│   ├── routing_filter.py            # 消息路由黑白名单过滤
│   └── signature_verify.py          # ECDSA签名、消息验签安全工具
├── config/                          # 全局配置目录
│   ├── federate_global.yaml         # 框架全局静态配置
│   ├── env_lan.yaml                 # 局域网联调配置
│   └── env_cloud.yaml               # 线上生产环境配置
├── docs/                            # 项目规范文档
│   ├── spec_v5.2.md                 # OpenClaw v5.2框架规范
│   ├── compliance_v5.0.md          # 合规校验规范文档
│   └── message_schema_v3.json       # 统一消息JSON Schema
├── scripts/                         # 运维辅助脚本
│   ├── gen_all_federate_cert.py     # 一键生成CA/客户端TLS证书脚本
│   ├── storage_quota_check.py        # 存储配额巡检脚本
│   └── federate_audit_query.py      # 审计日志查询工具
├── tests/                           # 测试用例目录
│   ├── unit/                        # 单元测试（消息、签名、合规工具）
│   └── federate_integration/        # 多智能体集成通信测试
├── federate_storage/                # 运行时自动生成：分层业务存储目录
├── .env.example                     # 环境变量模板（MQTT地址、证书路径、Agent标识）
├── .gitignore                       # Git忽略文件清单
├── requirements.txt                # Python第三方依赖清单
└── start_federate.py                # 项目统一启动入口（通过--role指定启动智能体）
```

## 三、环境部署教程（Windows本地开发，无需Docker）
### 3.1 前置依赖安装
1. 本地安装 Python3.10 及以上版本
2. 全局一键安装所有第三方依赖
```bash
pip install -r requirements.txt
```

### 3.2 环境变量配置
复制环境模板，生成本地私有配置文件（.env不会提交至Git）
```bash
# Windows CMD
copy .env.example .env
```
可修改核心配置项：
- `BUS_MQ_HOST`：MQTT消息服务IP地址
- `BUS_MQ_PORT`：MQTT端口（无加密1883 / TLS加密8883）
- `AGENT_ID`：当前本机智能体唯一标识
- `CERT_ROOT_PATH`：TLS证书存放目录

## 四、项目启动方式
### 4.1 启动全局核心：架构智能体（必须最先启动）
```bash
python start_federate.py --role arch
```

### 4.2 启动其他业务智能体（新开CMD窗口独立运行）
```bash
# 管控智能体
python start_federate.py --role ceo

# 项目智能体
python start_federate.py --role pm

# 算法智能体
python start_federate.py --role algorithm

# 平台运维智能体
python start_federate.py --role platform

# 市场业务智能体
python start_federate.py --role market
```

## 五、两种开发模式说明
### 模式1：纯代码调试模式（推荐本地写代码，无需EMQX）
无需启动任何消息中间件，屏蔽MQTT真实网络连接，仅测试类逻辑、文件存储、合规校验代码。
操作：打开 `core/federate_bus.py`，注释connect方法内所有MQTT连接代码，启用模拟总线逻辑。
限制：无法实现多智能体互相收发消息，仅用于框架代码调试。

### 模式2：真实分布式联调（多机/多窗口通信）
需要本地安装 Windows 独立版 EMQX 消息中间件，默认开放1883端口；
1. 调试环境：注释TLS证书加载代码，无需证书即可通信；
2. 生产环境：执行证书脚本 `scripts/gen_all_federate_cert.py` 生成全套CA与客户端证书，开启TLS加密传输。

### 模式3：线上服务器部署（Docker）
项目内置deploy/docker-compose.yml，服务器环境可一键拉起EMQX容器，统一环境，仅线上部署使用，本地开发可删除deploy目录。

## 六、第三方依赖说明
| 依赖包 | 作用 |
| ---- | ---- |
| paho-mqtt | MQTT消息总线通信核心库 |
| python-dotenv | 读取.env环境变量配置 |
| ecdsa / cryptography | 实现消息ECDSA签名、TLS证书加密能力 |
| pyyaml / jsonschema | 读取yaml配置、校验消息结构合法性 |
| requests / tqdm | 文件传输、进度条等辅助工具 |

## 七、开发规范
1. 分支管理：
   - `main`：稳定可上线主干分支，禁止直接push；
   - `dev-collab`：日常开发、框架迭代分支，功能完成后合并至main；
2. 新增智能体规范：
   - 在agents下新建独立文件夹，创建xx_main.py；
   - 继承BaseFederateAgent基类，重写bind_task_callback注册消息回调；
3. 提交规范：commit信息统一格式 `[分类] 内容描述`，如`[新增] 市场智能体报表逻辑`、`[优化] 完善README文档`。

## 八、常见问题
1. 启动提示证书文件不存在
    本地调试使用模拟总线注释TLS代码；生产运行执行证书生成脚本。
2. MQTT连接超时Timeout
    未启动EMQX中间件，或.env内MQ_HOST地址填写错误。
3. 导入模块红线报错
    VS Code配置python.analysis.extraPaths添加项目根目录，重启语言服务。

