
# My implementation
queue_size = 4
jack_queue = [None for index in range(0, queue_size)]  # [None, 8, 7, 10] FIFO
rear_pointer = queue_size - 1  # rear pointer is the last one


def en_queue(item):
    global rear_pointer, jack_queue
    # 确认容量是否为满
    if rear_pointer != -1:
        jack_queue[rear_pointer] = item
        rear_pointer -= 1
    else:
        print("CIE-Queue is full")


def de_queue():
    global rear_pointer, jack_queue, queue_size
    # 确认是否为空
    if rear_pointer != queue_size - 1:  # 不等于 queue size 的时候既是空的
        out_item = jack_queue[-1]  # 刷新进制，所以最后一个永远是进去的第一个
        current_i = queue_size - 1
        while current_i != -1:
            jack_queue[current_i] = jack_queue[current_i - 1]
            current_i -= 1
            if jack_queue[current_i - 1] is None:
                rear_pointer += 1
                jack_queue[current_i] = None
                return out_item
        # queue已满，处理第一个数
        jack_queue[0] = None
        rear_pointer += 1
        return out_item
    else:
        print("CIE-Queue is empty")


en_queue(10)
en_queue(7)
en_queue(8)
en_queue(9)
print(jack_queue)
print(de_queue(), jack_queue)
print(de_queue(), jack_queue)
print(de_queue(), jack_queue)
print(de_queue(), jack_queue)
en_queue(10)
print(jack_queue)