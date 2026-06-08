
# 左头右尾
my_linked_list = [16, 19, 20, None, None]  # linked_list index = pointer position
linked_list_pointer = [1, 2, 3, 4, -1]
startPointer = 0  # The head of the linked list
heapStartPointer = 3


# 从小到大连接在一起的linked list
def insert(add_item):
    global startPointer, heapStartPointer
    if heapStartPointer == -1:
        print("Linked list full")
    else:
        last_pointer = startPointer
        pre_pointer = -1
        next_pointer = startPointer
        pre_pos = -1
        while my_linked_list[last_pointer] is not None:
            pre_pointer = last_pointer
            last_pointer = linked_list_pointer[last_pointer]
        if add_item >= my_linked_list[pre_pointer]:
            my_linked_list[heapStartPointer] = add_item  # 插入数值
            heapStartPointer = linked_list_pointer[heapStartPointer]
        else:
            while add_item >= my_linked_list[next_pointer]:
                pre_pos = next_pointer
                next_pointer = linked_list_pointer[next_pointer]
            # 刷新最大数值的index
            tem_heap = linked_list_pointer[heapStartPointer]
            linked_list_pointer[pre_pointer] = linked_list_pointer[last_pointer]
            # 插入数值
            my_linked_list[heapStartPointer] = add_item
            # 连接前链
            linked_list_pointer[pre_pos] = heapStartPointer
            # 连接后链
            linked_list_pointer[heapStartPointer] = next_pointer
            # 刷新空位置
            heapStartPointer = tem_heap
            return last_pointer, pre_pointer


print(insert(17))
print(insert(21))
print(my_linked_list, linked_list_pointer)
print(heapStartPointer)
