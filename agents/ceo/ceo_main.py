from agents.base_federate_agent import BaseFederateAgent

class CeoAgent(BaseFederateAgent):
    def bind_task_callback(self):
        self.bus.register_msg_callback("EVENT.ALARM", self.handle_compliance_alarm)

    def handle_compliance_alarm(self, msg):
        print(f"[CEO合规总督] 收到全局告警：{msg['content']['payload']}")