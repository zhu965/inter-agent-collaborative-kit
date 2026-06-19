from agents.base_federate_agent import BaseFederateAgent

class PlatformAgent(BaseFederateAgent):
    def bind_task_callback(self):
        self.bus.register_msg_callback("edge_deploy", self.handle_edge_deploy)

    def handle_edge_deploy(self, msg):
        print(f"[Platform] 边缘部署任务 {msg}")