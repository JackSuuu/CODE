# 从小到大的链表
# 要求：Linkedlist
# 按照从小到大的顺序排列，startPointer指向最小值节点
# 1、LinkedList长度为5，执行addNode添加5个数：1，3，4，7，8
# 2、delete() 执行四次，分别删除1、4，8和99，然后print出整个linkedlist
#       delete() 返回删除节点的index值，-1 表示未找到
# 3、添加四个数：2，5，10，11。并打印出整个linkedlist
Linked_List = [None for _ in range(5)]  # [1, 2, 4, None, None]
Linked_List_Pointer = [1, 2, 3, 4, -1]  # [0, 2, -1, 4, -1]
start_pointer = -1
heap_start_pointer = 0
# Linked list 有两条链，值链和空链，值链使用start pointer开始索引，空链使用heap start pointer开始索引


def check():
    print(Linked_List)
    print(Linked_List_Pointer)
    print(f"start pointer: {start_pointer}")
    print(f"heap start pointer: {heap_start_pointer}")


def insert(item):
    global start_pointer, heap_start_pointer
    if heap_start_pointer == -1:
        return "---Linked List is FULL---"
    else:
        # 处理起始情况
        if start_pointer == -1:
            start_pointer = heap_start_pointer
            heap_start_pointer = Linked_List_Pointer[heap_start_pointer]
            Linked_List[start_pointer] = item
            Linked_List_Pointer[start_pointer] = -1
            return "Insert Successfully"
        else:
            # 值插入
            Linked_List[heap_start_pointer] = item
            # 找到现在的节点和前一个节点的位置
            current_pointer = start_pointer
            pre_pointer = -1
            tem_heap = Linked_List_Pointer[heap_start_pointer]
            while current_pointer != -1:
                if Linked_List[current_pointer] > item:
                    # 最小
                    if pre_pointer == -1:
                        Linked_List_Pointer[heap_start_pointer] = start_pointer
                        start_pointer = heap_start_pointer
                    # 中间
                    else:
                        Linked_List_Pointer[pre_pointer] = heap_start_pointer
                        Linked_List_Pointer[heap_start_pointer] = current_pointer
                    heap_start_pointer = tem_heap
                    break
                # 刷新
                pre_pointer = current_pointer
                current_pointer = Linked_List_Pointer[current_pointer]
            # 最大
            if current_pointer == -1:
                Linked_List_Pointer[pre_pointer] = heap_start_pointer
                Linked_List_Pointer[heap_start_pointer] = -1
                heap_start_pointer = tem_heap
            return "Insert Successfully"


print("------------------------------------------------------")
insert(1)
insert(2)
# insert(4)
# insert(7)
# insert(8)
insert(11)
check()


def delete(item):
    global start_pointer, heap_start_pointer
    if start_pointer == -1:
        return "---Linked List is EMPTY---"
    else:
        current_pointer = start_pointer
        pre_pointer = -1
        while current_pointer != -1:
            if Linked_List[current_pointer] == item:
                Linked_List[current_pointer] = None
                tem = heap_start_pointer
                heap_start_pointer = current_pointer
                if pre_pointer == -1:
                    start_pointer = Linked_List_Pointer[start_pointer]
                else:
                    next_pointer = Linked_List_Pointer[current_pointer]
                    Linked_List_Pointer[pre_pointer] = Linked_List_Pointer[next_pointer]
                Linked_List_Pointer[heap_start_pointer] = tem
                break
            else:
                pre_pointer = current_pointer
                current_pointer = Linked_List_Pointer[current_pointer]
        if current_pointer == -1:
            return "NOT FOUND"


print("-------------")
delete(11)
delete(2)
print(delete(11))
check()
