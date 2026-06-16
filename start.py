"""
inter-agent-collaborative-kit 项目统一启动入口
功能：加载配置、初始化消息总线、启动多智能体协同服务
"""
import os
from dotenv import load_dotenv
from core.message_bus import MessageBus
from core.agent_manager import AgentManager
from config.load_config import load_all_config

# 加载环境变量模板
load_dotenv()

def main():
    print("===== Inter-Agent Collaborative Kit 启动 =====")
    # 加载全局配置、智能体专属配置
    global_cfg, agent_cfg = load_all_config()
    # 初始化跨智能体消息总线
    bus = MessageBus(
        host=os.getenv("MESSAGE_BUS_HOST"),
        port=int(os.getenv("MESSAGE_BUS_PORT"))
    )
    # 智能体管理器初始化、注册全部业务智能体
    agent_mgr = AgentManager(message_bus=bus)
    agent_mgr.register_all_agents()
    # 启动多智能体协同调度循环
    agent_mgr.run_collaboration()

if __name__ == "__main__":
    main()