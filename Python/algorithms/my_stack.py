

class Stack:
    def __init__(self):
        self.item = None
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    # Return the top item, but not remove it
    def peak(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def base_converter(dec_num, base_num):
    ans_char = "0123456789ABCDEF"
    rem_stack = Stack()

    while dec_num > 0:
        rem = dec_num % base_num
        rem_stack.push(rem)
        dec_num = dec_num // base_num
    ans_str = ""

    while not rem_stack.is_empty():
        ans_str = ans_str + ans_char[rem_stack.pop()]
    return ans_str


dec_num_input = int(input("decimal number: "))
base_num_input = int(input("convert to what base: "))

print(f"decimal number {dec_num_input} in base {base_num_input} is {base_converter(dec_num_input, base_num_input)}")