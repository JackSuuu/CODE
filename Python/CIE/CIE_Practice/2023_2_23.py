
# (a)
ArrayNodes = [[-1 for X in range(3)] for Y in range(20)]
RootPointer = -1  # integer
FreeNode = 0  # integer


# (b)
def AddNode(node_data):
    global ArrayNodes, RootPointer, FreeNode
    # node_data = int(input("Please Enter the data: "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = node_data
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            placed = False
            current_node = RootPointer
            while not placed:
                if node_data < ArrayNodes[current_node][1]:
                    if ArrayNodes[current_node][0] == -1:
                        ArrayNodes[current_node][0] = FreeNode
                        placed = True
                    else:
                        current_node = ArrayNodes[current_node][0]
                else:
                    if ArrayNodes[current_node][2] == -1:
                        ArrayNodes[current_node][2] = FreeNode
                        placed = True
                    else:
                        current_node = ArrayNodes[current_node][2]
        FreeNode += 1
    else:
        print("tree capacity full")
    return RootPointer, FreeNode


# (c)
def PrintAll():
    for row in ArrayNodes:
        for each in row:
            print(each, end=' ')
        print('\n')


# (d)(i)
test_data = [10, 5, 15, 8, 12, 6, 20, 11, 9, 4] 
for i in range(10):
    AddNode(test_data[i])

PrintAll()


# (d)(ii)
# 左 --> 根 --> 右
def inOrder(Array_Nodes, rootNode):
    if Array_Nodes[rootNode][0] != -1:
        inOrder(Array_Nodes, ArrayNodes[rootNode][0])
    print(str(Array_Nodes[rootNode][1]))
    if ArrayNodes[rootNode][2] != -1:
        inOrder(Array_Nodes, ArrayNodes[rootNode][2])


inOrder(ArrayNodes, rootNode=0)
