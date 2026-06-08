import random

# 模拟不同类型的服务器节点
class ServerNode:
    def __init__(self, name, cpu_power):
        self.name = name
        self.cpu_power = cpu_power

# 一些异构的服务器节点
node1 = ServerNode("Node1", 80)
node2 = ServerNode("Node2", 100)
node3 = ServerNode("Node3", 120)

# 模拟应用任务
class ApplicationTask:
    def __init__(self, name):
        self.name = name

# 一些应用任务
task1 = ApplicationTask("Task1")
task2 = ApplicationTask("Task2")

# 模拟收集 CPU 使用数据
def collect_cpu_data(task, node):
    return random.randint(10, node.cpu_power)  # 简化的模拟数据

# 模拟机器学习分类（这里只是简单示意）
def classify_task(task):
    if task.name == "Task1":
        return "Type1"
    else:
        return "Type2"

# 评估和建模部分（简化示意）
task1_data = collect_cpu_data(task1, node1)
task2_data = collect_cpu_data(task2, node2)

task1_class = classify_task(task1)
task2_class = classify_task(task2)

print(f"Task1 on {node1.name} has CPU data: {task1_data}, classified as {task1_class}")
print(f"Task2 on {node2.name} has CPU data: {task2_data}, classified as {task2_class}")