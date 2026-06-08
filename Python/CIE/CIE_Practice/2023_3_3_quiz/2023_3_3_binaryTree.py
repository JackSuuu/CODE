# Binary Tree 数组实现 + Class实现
# 数组方式：一个二维数组，7行3列
# Class方式：定义一个Node的Class（value, left, right），初始化出N个节点，然后把节点存入一个数组中
# 要求：
# 1、Binary Tree长度为7，执行addNode添加8个数：10,7,12,8,4,11,15,3
# 2、分别执行preOrder、inOrder和postOrder打印出Binary Tree

# Array
Tree_init = [[0 for X in range(3)] for Y in range(7)]

root_node = 0
root_pointer = -1
freeNode = 0


def addNode(ArrayNode: Tree_init, Node_Data: int):
    global root_pointer, freeNode
    if freeNode < 7:
        ArrayNode[freeNode][0] = -1
        ArrayNode[freeNode][1] = Node_Data
        ArrayNode[freeNode][2] = -1
        if root_pointer == -1:  # Base case, if tree is empty
            root_pointer = freeNode
        else:
            Placed = False
            current_Node = root_pointer
            while not Placed:
                if Node_Data < ArrayNode[current_Node][1]:
                    if ArrayNode[current_Node][0] == -1:
                        ArrayNode[current_Node][0] = freeNode
                        Placed = True
                    else:
                        current_Node = ArrayNode[current_Node][0]
                else:
                    if ArrayNode[current_Node][2] == -1:
                        ArrayNode[current_Node][2] = freeNode
                        Placed = True
                    else:
                        current_Node = ArrayNode[current_Node][2]
        freeNode += 1
    else:
        return "Tree is FULL"
    return ArrayNode


addNode(Tree_init, 10)
addNode(Tree_init, 7)
addNode(Tree_init, 12)
addNode(Tree_init, 8)
addNode(Tree_init, 4)
addNode(Tree_init, 11)
addNode(Tree_init, 15)
print(addNode(Tree_init, 3))
print(Tree_init)
print(f"Free Node: {freeNode}")


# root -> left -> right
def preOrder(ArrayNode, free_Node):
    print(str(ArrayNode[free_Node][1]))
    if ArrayNode[free_Node][0] != -1:
        preOrder(ArrayNode, ArrayNode[free_Node][0])
    if ArrayNode[free_Node][2] != -1:
        preOrder(ArrayNode, ArrayNode[free_Node][2])


print("-----------------PRE ORDER------------------")
preOrder(Tree_init, root_node)


# left -> root -> right
def InOrder(ArrayNode, free_Node):
    if ArrayNode[free_Node][0] != -1:
        InOrder(ArrayNode, ArrayNode[free_Node][0])
    print(str(ArrayNode[free_Node][1]))
    if ArrayNode[free_Node][2] != -1:
        InOrder(ArrayNode, ArrayNode[free_Node][2])


print("-----------------IN ORDER------------------")
InOrder(Tree_init, root_node)


# left -> root -> right
def PostOrder(ArrayNode, free_Node):
    if ArrayNode[free_Node][0] != -1:
        PostOrder(ArrayNode, ArrayNode[free_Node][0])
    if ArrayNode[free_Node][2] != -1:
        PostOrder(ArrayNode, ArrayNode[free_Node][2])
    print(str(ArrayNode[free_Node][1]))


print("-----------------POST ORDER------------------")
PostOrder(Tree_init, root_node)
