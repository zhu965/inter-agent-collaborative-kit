from agents.base_federate_agent import BaseFederateAgent

class MarketAgent(BaseFederateAgent):
    def bind_task_callback(self):
        self.bus.register_msg_callback("market_analysis", self.handle_market_report)

    def handle_market_report(self, msg):
        print(f"[Market] 市场分析报告接收 {msg}")