
#   10
#  /  \
# 5   16

Tree_init = [[0 for X in range(3)] for Y in range(20)]  # 初始化20个节点
binaryTree = [[1, 10, 2], [-1, 5, -1], [-1, 16, -1], [None, None, None]]

root_pointer = -1
root_node = 0
freeNode = 3


# 根 → 左 → 右
def preOrder(ArrayNodes, free_node):  # 前序遍历
    print(str(ArrayNodes[free_node][1]))
    if ArrayNodes[free_node][0] != -1:
        preOrder(ArrayNodes, ArrayNodes[free_node][0])
    if ArrayNodes[free_node][2] != -1:
        preOrder(ArrayNodes, ArrayNodes[free_node][2])


preOrder(binaryTree, root_node)


# 左 → 根 → 右
def InOrder(ArrayNodes, free_node):  # 中序遍历
    if ArrayNodes[free_node][0] != -1:
        InOrder(ArrayNodes, ArrayNodes[free_node][0])
    print(str(ArrayNodes[free_node][1]))
    if ArrayNodes[free_node][2] != -1:
        InOrder(ArrayNodes, ArrayNodes[free_node][2])


# 左 → 右 → 根
def postOrder(ArrayNodes, free_node):  # 后序遍历
    if ArrayNodes[free_node][0] != -1:
        postOrder(ArrayNodes, ArrayNodes[free_node][0])
    if ArrayNodes[free_node][2] != -1:
        postOrder(ArrayNodes, ArrayNodes[free_node][2])
    print(str(ArrayNodes[free_node][1]))


# postOrder(binaryTree, free_node)


def addNode(ArrayNodes, free_node):
    global root_pointer
    NodeData = int(input("Enter the data:"))
    if free_node <= 19:
        ArrayNodes[free_node][0] = -1
        ArrayNodes[free_node][1] = NodeData
        ArrayNodes[free_node][2] = -1
        if root_pointer == -1:
            root_pointer = free_node
        else:
            placed = False
            currentNode = root_pointer
            while not placed:  # BIGGEST MISTAKE -- 2023/3/21 MOCK
                if NodeData < ArrayNodes[currentNode][1]:
                    if ArrayNodes[currentNode][0] == -1:
                        ArrayNodes[currentNode][0] = free_node
                        placed = True
                    else:
                        currentNode = ArrayNodes[currentNode][0]
                else:
                    if ArrayNodes[currentNode][2] == -1:
                        ArrayNodes[currentNode][2] = free_node
                        placed = True
                    else:
                        currentNode = ArrayNodes[currentNode][2]
        free_node += 1
    else:
        print("The Binary Tree is full")
    return ArrayNodes, free_node


addNode(binaryTree, freeNode)
print(binaryTree)
