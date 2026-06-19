import argparse
import os
from dotenv import load_dotenv

# 加载全局环境变量
load_dotenv(".env.example")

# 导入各角色智能体主程序
from agents.base_federate_agent import BaseFederateAgent
from agents.arch.arch_main import ArchAgent
from agents.ceo.ceo_main import CeoAgent
from agents.pm.pm_main import PmAgent
from agents.algorithm.algo_main import AlgorithmAgent
from agents.platform.platform_main import PlatformAgent
from agents.market.market_main import MarketAgent

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OpenClaw联邦智能体统一启动入口")
    parser.add_argument("--role", required=True, choices=["arch", "ceo", "pm", "algorithm", "platform", "market"],
                        help="指定启动智能体角色")
    args = parser.parse_args()

    match args.role:
        case "arch":
            print("===== 启动架构智能体：总线+注册中心+存储管理 =====")
            agent = ArchAgent()
        case "ceo":
            print("===== 启动CEO总督智能体：证书签发+合规审计 =====")
            agent = CeoAgent()
        case "pm":
            print("===== 启动PM产品智能体 =====")
            agent = PmAgent()
        case "algorithm":
            print("===== 启动算法智能体 =====")
            agent = AlgorithmAgent()
        case "platform":
            print("===== 启动平台部署智能体 =====")
            agent = PlatformAgent()
        case "market":
            print("===== 启动市场智能体 =====")
            agent = MarketAgent()
        case _:
            raise Exception("不支持的智能体角色")

    # 智能体初始化、连接总线、循环监听消息
    agent.init_federate()
    agent.run_consume_loop()