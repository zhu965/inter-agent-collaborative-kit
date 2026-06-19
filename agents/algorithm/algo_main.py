from agents.base_federate_agent import BaseFederateAgent

class AlgorithmAgent(BaseFederateAgent):
    def bind_task_callback(self):
        self.bus.register_msg_callback("dataset_delivery", self.handle_dataset)

    def handle_dataset(self, msg):
        print(f"[Algorithm] 数据集任务接收 {msg}")
        # 数据集上传示例调用
        # self.federate_upload("dataset_delivery", "./tmp/dataset.zip", meta=msg["audit"])