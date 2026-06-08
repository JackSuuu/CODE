
# Stack list implementation
stack = [None for index in range(0, 10)]
basePointer = 0
topPointer = -1  # -1 means nothing, pointer means the index
stackFull = 10
item = None


def push(item):
    global topPointer, stackFull  # use the global variable inside the function
    if topPointer < stackFull - 1:  # 最大 index 数量 - 1
        topPointer += 1
        stack[topPointer] = item
    else:
        print("Stack is full")


def pop():
    global topPointer, stackFull, stack
    if topPointer != -1:
        pop_item = stack[topPointer]
        topPointer -= 1
        return pop_item
    else:
        print("Stack is empty")


# Stack class implementation
class Stack:
    def __init__(self, stack_size):
        self.stack = [None for _ in range(stack_size)]
        self.topPointer = -1
        self.stack_size = stack_size

    def push(self, push_item):
        if self.topPointer < self.stack_size - 1:
            self.topPointer += 1
            self.stack[self.topPointer] = push_item
        else:
            print("Stack is full")

    def pop(self):
        if self.topPointer != -1:
            pop_item = self.stack[self.topPointer]
            self.topPointer -= 1
            return pop_item
        else:
            print("Stack is empty")


j_stack = Stack(10)
j_stack.push(19)
print(j_stack.pop())
