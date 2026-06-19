from agents.base_federate_agent import BaseFederateAgent

class ArchAgent(BaseFederateAgent):
    def bind_task_callback(self):
        # 架构监听部署、审计、文件上传事件
        self.bus.register_msg_callback("EVENT.FILE_UPLOAD", self.handle_file_upload_event)

    def handle_file_upload_event(self, msg):
        print(f"[Arch 存储管理] 收到文件上传事件：{msg['content']['payload']}")