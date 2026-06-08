# class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = 0
        self.right = 0


Class_Tree_init = [Node(0) for _ in range(7)]

root_node = 0
root_pointer = -1
freeNode = 0


def addNode(ArrayNode: Class_Tree_init, Node_Data: int):
    global root_pointer, freeNode
    if freeNode < 7:
        ArrayNode[freeNode].left = -1
        ArrayNode[freeNode].data = Node_Data
        ArrayNode[freeNode].right = -1
        if root_pointer == -1:  # Base case, if tree is empty
            root_pointer = freeNode
        else:
            Placed = False
            current_Node = root_pointer
            while not Placed:
                if Node_Data < ArrayNode[current_Node].data:
                    if ArrayNode[current_Node].left == -1:
                        ArrayNode[current_Node].left = freeNode
                        Placed = True
                    else:
                        current_Node = ArrayNode[current_Node].left
                else:
                    if ArrayNode[current_Node].right == -1:
                        ArrayNode[current_Node].right = freeNode
                        Placed = True
                    else:
                        current_Node = ArrayNode[current_Node].right
        freeNode += 1
    else:
        return "Tree is FULL"
    return ArrayNode


addNode(Class_Tree_init, 10)
addNode(Class_Tree_init, 7)
addNode(Class_Tree_init, 12)
addNode(Class_Tree_init, 8)
addNode(Class_Tree_init, 4)
addNode(Class_Tree_init, 11)
addNode(Class_Tree_init, 15)
print(addNode(Class_Tree_init, 3))
print(Class_Tree_init)
print(f"Free Node: {freeNode}")


# root -> left -> right
def preOrder(ArrayNode, free_Node):
    print(str(ArrayNode[free_Node].data))
    if ArrayNode[free_Node].left != -1:
        preOrder(ArrayNode, ArrayNode[free_Node].left)
    if ArrayNode[free_Node].right != -1:
        preOrder(ArrayNode, ArrayNode[free_Node].right)


print("-----------------PRE ORDER------------------")
preOrder(Class_Tree_init, root_node)


# 其他两个order就不写了，要是preorder是对的，其他应该也没什么问题。
