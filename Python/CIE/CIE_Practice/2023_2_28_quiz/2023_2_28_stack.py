
# Stack
#  Stack 数组实现 + Class实现（push和pop封装在class里）
#  要求：
# 1、Stack长度为5，执行push添加5个数：5，6，7，1，2
# 2、pop出来两个数，并打印出来
# 3、push三个数：8，9，10
# 4、执行pop函数6次，并打印出pop出来的内容

# Stack Array stack Implementation
array_stack = [-1 for _ in range(5)]
top_pointer = -1
stack_full = 5


def push(item: int):
    global array_stack, top_pointer
    if top_pointer != stack_full - 1:
        top_pointer += 1
        array_stack[top_pointer] = item
    else:
        print("Stack is full already")


def pop():
    global array_stack, top_pointer
    if top_pointer != -1:
        pop_item = array_stack[top_pointer]
        top_pointer -= 1
        return pop_item
    else:
        return "Stack is empty already"


# push(5)
# push(6)
# push(7)
# push(1)
# push(2)
# print(array_stack)
# print(pop())
# print(pop())
# push(8)
# push(9)
# push(10)
# for i in range(6):
#     print(pop())


# Stack Class Implementation
class JackStack:
    def __init__(self, stack_size=5):
        self.array_stack = [-1 for _ in range(stack_size)]
        self.top_pointer = -1
        self.stack_full = stack_size

    def push(self, item):
        if self.top_pointer != stack_full - 1:
            self.top_pointer += 1
            self.array_stack[self.top_pointer] = item
        else:
            print("Stack is full already")

    def pop(self):
        if self.top_pointer != -1:
            pop_item = self.array_stack[self.top_pointer]
            self.top_pointer -= 1
            return pop_item
        else:
            return "Stack is empty already"


Jack_stack = JackStack(stack_size=5)
Jack_stack.push(5)
Jack_stack.push(6)
Jack_stack.push(7)
Jack_stack.push(1)
Jack_stack.push(2)
print(Jack_stack.array_stack)
print(Jack_stack.pop())
print(Jack_stack.pop())
Jack_stack.push(8)
Jack_stack.push(9)
Jack_stack.push(10)
for i in range(6):
    print(Jack_stack.pop())
