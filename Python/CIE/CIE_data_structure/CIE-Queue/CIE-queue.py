# CIE queue example
# 左进左出
myqueue = [None for index in range(0, 4)]  # [None, None, None, None]
frontPointer = 0
rearPointer = -1
queueFull = 4
queueLength = 0


# [1, None, None, None]
def enQueue(item):
    global queueLength, rearPointer
    if queueLength < queueFull:
        if rearPointer < len(myqueue) - 1:
            rearPointer += 1
        else:
            rearPointer = 0
        queueLength = queueLength + 1
        myqueue[rearPointer] = item
    else:
        return "Queue is full, cannot enqueue"


# [1, 2, 3, 4] 1 goes out first
def deQueue():
    global queueLength, frontPointer
    if queueLength != 0:
        de_item = myqueue[frontPointer]
        myqueue[frontPointer] = None
        if frontPointer == len(myqueue) - 1:
            frontPointer = 0
        else:
            frontPointer += 1
        queueLength -= 1
        return de_item
    else:
        return "Queue is empty, cannot dequeue"


enQueue(1)
enQueue(2)
enQueue(3)
enQueue(4)
print(myqueue)
print(queueLength)
deQueue()
print(myqueue)
deQueue()
print(myqueue)
deQueue()
print(myqueue)
