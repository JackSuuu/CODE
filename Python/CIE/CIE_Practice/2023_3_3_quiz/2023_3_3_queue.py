# Queue 数组实现 + Class实现（Enqueue和Dequeue封装在Clas里）
# 要求：
# 1、Queue长度为5，执行Enqueue添加5个数：5，6，7，1，2
# 2、Dequeue出来两个数，并打印出来
# 3、Enqueue三个数：8，9，10
# 4、执行Dequeue函数6次，并打印出Dequeue出来的内容


class JackQueue:
    def __init__(self):
        self._Queue_ = [None for _ in range(5)]
        self.frontPointer = -1
        self.rearPointer = -1
        self.queueFull = 5
        self.queueLength = 0

    def enQueue(self, item):
        if self.queueLength < self.queueFull:
            self._Queue_[self.frontPointer] = item
            if self.frontPointer != - self.queueFull:
                self.frontPointer -= 1
            else:
                self.frontPointer = -1
            self.queueLength += 1
        else:
            return "Queue is FULL"

    def deQueue(self):
        if self.queueLength != 0:
            de_item = self._Queue_[self.rearPointer]
            self._Queue_[self.rearPointer] = None
            if self.rearPointer != - self.queueFull:
                self.rearPointer -= 1
            else:
                self.rearPointer = -1
            self.queueLength -= 1
            return de_item
        else:
            return "Queue is EMPTY"

    def check(self):
        print(self._Queue_)
        print(f"Front Pointer: {self.frontPointer}")
        print(f"Rear Pointer: {self.rearPointer}")
        print(f"Queue Length: {self.queueLength}")


Jack_Queue = JackQueue()
Jack_Queue.enQueue(5)
Jack_Queue.enQueue(6)
Jack_Queue.enQueue(7)
Jack_Queue.enQueue(1)
Jack_Queue.enQueue(2)
Jack_Queue.check()
print("---------------------------")
print(Jack_Queue.deQueue())
print(Jack_Queue.deQueue())
Jack_Queue.check()
print("---------------------------")
Jack_Queue.enQueue(8)
Jack_Queue.enQueue(9)
print(Jack_Queue.enQueue(10))
Jack_Queue.check()
print("---------------------------")
for i in range(6):
    print(Jack_Queue.deQueue())
print("---------------------------")
Jack_Queue.check()
