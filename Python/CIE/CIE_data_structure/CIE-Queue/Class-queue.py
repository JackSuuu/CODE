
# [0, 1, 2, 3]
class Myqueue:
    def __init__(self, size):
        self.myqueue = [None for _ in range(size)]
        self.front_pointer = 0
        self.rear_pointer = -1
        self.queue_size = size
        self.queue_length = 0

    def enQueue(self, item):
        if self.queue_length < self.queue_size:
            if self.rear_pointer != self.queue_size - 1:
                self.rear_pointer += 1
            else:
                self.rear_pointer = 0
            self.myqueue[self.rear_pointer] = item
            self.queue_length += 1
        else:
            return "Queue is full"

    def deQueue(self):
        if self.queue_length > 0:
            de_item = self.myqueue[self.front_pointer]
            self.myqueue[self.front_pointer] = None
            if self.front_pointer != self.queue_size - 1:
                self.front_pointer += 1
            else:
                self.front_pointer = 0
            self.queue_length -= 1
            return de_item
        else:
            return "Queue is empty"


Queue_1 = Myqueue(4)
print(Queue_1.deQueue())
Queue_1.enQueue(0)
Queue_1.enQueue(1)
Queue_1.enQueue(2)
Queue_1.enQueue(3)
print(Queue_1.myqueue)
Queue_1.deQueue()
print(Queue_1.myqueue)
Queue_1.enQueue(4)
print(Queue_1.myqueue)
print(Queue_1.enQueue(4))
