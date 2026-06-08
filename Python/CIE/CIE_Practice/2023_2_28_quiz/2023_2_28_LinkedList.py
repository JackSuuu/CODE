# LinkedList （数组实现 + Class实现）
# 数组方式：两个数组，一个存值，一个存pointer
# Class方式：定义一个Node的Class，初始化出N个节点，然后把节点存入一个数组中

# 要求：Linkedlist
# 按照从小到大的顺序排列，startPointer指向最小值节点
# 1、LinkedList长度为5，执行addNode添加5个数：1，3，4，7，8
# 2、delete() 执行四次，分别删除1、4，8和99，然后print出整个linkedlist
#       delete() 返回删除节点的index值，-1 表示未找到
# 3、添加四个数：2，5，10，11。并打印出整个linkedlist


# LinkedList Array Implementation
list_size = 5
Array_Linked_List = [None for _ in range(list_size)]  # [1, None, None, None, None]
Array_Pointer = [1, 2, 3, 4, -1]
start_pointer = 0  # start pointer 指向的是最小的
heap_start_pointer = 0  # 如果从小到大，heap start pointer 前一个肯定指向的是最大的
list_current_size = 0


def check():
    print(Array_Linked_List)
    print(Array_Pointer)
    print(f"start pointer: {start_pointer}")
    print(f"heap start pointer: {heap_start_pointer}")


def find(item):
    curr_pointer = start_pointer
    pre_curr_pointer = -1
    while curr_pointer != -1:
        if Array_Linked_List[curr_pointer] == item:
            return curr_pointer, pre_curr_pointer
        else:
            pre_curr_pointer = curr_pointer
            curr_pointer = Array_Pointer[curr_pointer]
    return False


def insert(item):
    global Array_Linked_List, Array_Pointer, start_pointer, heap_start_pointer, list_current_size
    if list_current_size == list_size:
        return "Linked List is full"
    else:
        if list_current_size == 0:
            Array_Linked_List[heap_start_pointer] = item
            heap_start_pointer = Array_Pointer[heap_start_pointer]
            list_current_size += 1
            return 'Insert successfully'
        last_pointer = start_pointer
        pre_last_pointer = -1
        while Array_Linked_List[last_pointer] is not None:
            pre_last_pointer = last_pointer
            last_pointer = Array_Pointer[last_pointer]
        # compare to the biggest number
        # 插入最后
        if item >= Array_Linked_List[pre_last_pointer]:
            Array_Linked_List[heap_start_pointer] = item
            heap_start_pointer = Array_Pointer[heap_start_pointer]
            list_current_size += 1
            return 'Insert successfully'
        else:
            front_pointer = start_pointer
            pre_front_pointer = -1
            while item >= Array_Linked_List[front_pointer]:
                pre_front_pointer = front_pointer
                front_pointer = Array_Pointer[front_pointer]
            # 插入前面
            if pre_front_pointer == -1:
                tem_heap = Array_Pointer[heap_start_pointer]
                # insert item
                pre_front_pointer = front_pointer
                start_pointer = heap_start_pointer
                Array_Linked_List[heap_start_pointer] = item
                Array_Pointer[heap_start_pointer] = pre_front_pointer
                # refresh the next empty position
                Array_Pointer[pre_last_pointer] = tem_heap
                heap_start_pointer = tem_heap
                list_current_size += 1
                return 'Insert successfully'
            # 插入中间
            else:
                tem_heap = Array_Pointer[heap_start_pointer]
                # insert item
                Array_Linked_List[heap_start_pointer] = item
                Array_Pointer[heap_start_pointer] = pre_last_pointer
                # connect front linkage
                Array_Pointer[pre_front_pointer] = heap_start_pointer
                # connect last linkage
                Array_Pointer[pre_last_pointer] = tem_heap
                # refresh the next empty position
                heap_start_pointer = tem_heap
                list_current_size += 1
                return 'Insert successfully'


# add node section
insert(3)
insert(1)
insert(4)
insert(7)
insert(8)
print(insert(11))
check()
print("------------------------------------------------------")
# print(Array_Linked_List, Array_Pointer, heap_start_Pointer)

print(find(1))


def delete(item):
    global Array_Linked_List, Array_Pointer, start_pointer, heap_start_pointer, list_current_size
    if find(item) is not False:
        list_current_size -= 1
        last_pointer = start_Pointer
        # 最后一个数值的位置
        while Array_Pointer[last_pointer] != -1:
            last_pointer = Array_Pointer[last_pointer]
        # 得到"删除值"的位置和"删除值"前一个位置
        delete_item_index, pre_item_index = find(item)
        if delete_item_index == start_Pointer:
            start_Pointer = Array_Pointer[start_Pointer]
        else:
            Array_Pointer[pre_item_index] = Array_Pointer[delete_item_index]
        # 设置现在的节点为空
        Array_Linked_List[delete_item_index] = None
        Array_Pointer[delete_item_index] = -1
        # 连接"前一个"的节点到"空"节点
        Array_Pointer[last_pointer] = delete_item_index
        if Array_Linked_List[last_pointer] is not None:
            heap_start_Pointer = delete_item_index
        return "Delete successfully"
    else:
        return -1, "Not found value in Linked List"


delete(1)
check()
delete(4)
check()
delete(8)
check()
delete(99)
print("List current size is" + str(list_current_size))
check()
print("------------------------------------------------------")

insert(2)
check()
insert(5)
check()
insert(10)
check()
print(insert(11))
check()

delete(10)
check()
