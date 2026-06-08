# LinkedList （数组实现 + Class实现）
# 数组方式：两个数组，一个存值，一个存pointer
# Class方式：定义一个Node的Class，初始化出N个节点，然后把节点存入一个数组中

# 要求：Linkedlist
# 按照从小到大的顺序排列，startPointer指向最小值节点
# 1、LinkedList长度为5，执行addNode添加5个数：1，3，4，7，8
# 2、delete() 执行四次，分别删除1、4，8和99，然后print出整个linkedlist
#       delete() 返回删除节点的index值，-1 表示未找到
# 3、添加四个数：2，5，10，11。并打印出整个linkedlist

My_Linked_List = [None for _ in range(5)]  # [1, None, None, None, None]
My_LinkedList_Pointer = [1, 2, 3, 4, -1]
startPointer = -1
nullPointer = -1
heapStartPointer = 0


def check():
    print(My_Linked_List)
    print(My_LinkedList_Pointer)
    print(f"Start pointer: {startPointer}")
    print(f"Heap start pointer: {heapStartPointer}")


def addNode(item):
    global startPointer, nullPointer, heapStartPointer
    if heapStartPointer != -1:
        prePointer = -1
        currentPointer = startPointer
        My_Linked_List[heapStartPointer] = item
        if startPointer == -1:
            startPointer = heapStartPointer
            heapStartPointer = My_LinkedList_Pointer[heapStartPointer]
            My_LinkedList_Pointer[startPointer] = -1
        else:
            while currentPointer != -1:
                if My_Linked_List[currentPointer] > item:
                    tem = My_LinkedList_Pointer[heapStartPointer]
                    if prePointer == -1:
                        My_LinkedList_Pointer[heapStartPointer] = startPointer
                        startPointer = heapStartPointer
                    else:
                        My_LinkedList_Pointer[prePointer] = heapStartPointer
                        My_LinkedList_Pointer[heapStartPointer] = currentPointer
                    heapStartPointer = tem
                    break
                prePointer = currentPointer
                currentPointer = My_LinkedList_Pointer[currentPointer]
            if currentPointer == nullPointer:
                tem = My_LinkedList_Pointer[heapStartPointer]
                My_LinkedList_Pointer[prePointer] = heapStartPointer
                My_LinkedList_Pointer[heapStartPointer] = -1
                heapStartPointer = tem
    else:
        print("FULL")


def delete(item):
    global startPointer, nullPointer, heapStartPointer
    if startPointer == -1:
        print("EMPTY")
    else:
        prePointer = -1
        currentPointer = startPointer
        while currentPointer != -1:
            if My_Linked_List[currentPointer] == item:
                My_Linked_List[currentPointer] = None
                tem = heapStartPointer
                if currentPointer == startPointer:
                    startPointer = My_LinkedList_Pointer[currentPointer]
                else:
                    My_LinkedList_Pointer[prePointer] = My_LinkedList_Pointer[currentPointer]
                heapStartPointer = currentPointer
                My_LinkedList_Pointer[heapStartPointer] = tem
            else:
                prePointer = currentPointer
                currentPointer = My_LinkedList_Pointer[currentPointer]


addNode(3)
addNode(1)
# addNode(4)
# addNode(3)
addNode(11)
check()
print("-----------------")
delete(11)
check()
