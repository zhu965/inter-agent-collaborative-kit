from agents.base_federate_agent import BaseFederateAgent

class PmAgent(BaseFederateAgent):
    def bind_task_callback(self):
        self.bus.register_msg_callback("prd_sync", self.handle_prd_sync)

    def handle_prd_sync(self, msg):
        print(f"[PM] 收到PRD同步消息 {msg}")
        # 业务生成PRD文件后调用 self.federate_upload 存入统一存储
        # store_path = self.federate_upload(task_type="prd_sync", local_file="xxx.md", meta=msg["audit"])