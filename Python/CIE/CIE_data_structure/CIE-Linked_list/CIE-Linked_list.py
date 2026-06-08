
# [None, None, None, None]
my_linked_list = [27, 19, 36, 42, 16, None, None, None, None, None, None, None]  # linked_list index = pointer position
linked_list_pointer = [-1, 0, 1, 2, 3, 6, 7, 8, 9, 10, 11, -1]  # 新加的是正序，加进入的是反序
startPointer = 4  # The head of the linked list
heapStartPointer = 5


def find(item):
    next_pointer = startPointer
    while next_pointer != -1:
        if my_linked_list[item] == item:
            return next_pointer
        else:
            next_pointer = linked_list_pointer[next_pointer]
    return -1


def insert(add_item):
    global startPointer, heapStartPointer
    if heapStartPointer == -1:
        print("Linked list full")
    else:
        # 从头插入 --> 插入数据
        my_linked_list[heapStartPointer] = add_item
        # 保存 Start pointer 以供后续链接
        headPointer = startPointer
        # 刷新 Start pointer
        startPointer = heapStartPointer
        # heap start pointer 指向下一个 linked list pointer
        heapStartPointer = linked_list_pointer[heapStartPointer]
        # 刷新 linked list pointer 指向前一个数据
        linked_list_pointer[startPointer] = headPointer


insert(99)
print(my_linked_list, linked_list_pointer)


def delete(delete_item):
    global startPointer, heapStartPointer
    if startPointer == -1:
        print("Linked List Empty")
    else:
        current_pointer = startPointer
        while current_pointer != -1:
            previous_pointer = current_pointer
            if my_linked_list[current_pointer] == delete_item:
                my_linked_list[current_pointer] = None
                # 将空 linked list 下一个值连接 heap start pointer
                next_pointer = linked_list_pointer[current_pointer]
                # 将本身改为 heap start pointer
                linked_list_pointer[current_pointer] = heapStartPointer
                heapStartPointer = current_pointer
                if current_pointer == startPointer:
                    startPointer = next_pointer
                else:
                    linked_list_pointer[previous_pointer] = next_pointer
                # 刷新下一个值
                current_pointer = linked_list_pointer[current_pointer]
