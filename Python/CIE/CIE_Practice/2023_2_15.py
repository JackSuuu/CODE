# CIE_真题/9618_s21_qp_41.pdf
# Question 1

class Node:
    # data: Integer
    # nextNode: Integer
    def __init__(self, data, next_node):
        self.data = data
        self.nextNode = next_node


linkedList = [Node(1, 1), Node(5, 4), Node(6, 7), Node(7, -1), Node(2, 2), Node(0, 6),
              Node(0, 8), Node(56, 3), Node(0, 9), Node(0, -1)]
emptyList = 5


def outputNodes(array: linkedList, start_pointer: int):
    current_pointer = start_pointer
    while current_pointer != -1:
        print(f"{array[current_pointer].data} --> {array[current_pointer].nextNode}")
        current_pointer = array[current_pointer].nextNode


outputNodes(linkedList, start_pointer=0)


# data to be added to the end of the linkedList.
def addNode(linked_list, start_pointer: int):
    global emptyList
    insert_item = int(input("Enter the data to add:"))
    if linked_list[emptyList].nextNode != -1:
        current_pointer = start_pointer
        while linked_list[current_pointer].nextNode != -1:
            current_pointer = linked_list[current_pointer].nextNode  # 3
        linked_list[current_pointer].nextNode = emptyList
        linked_list[emptyList].data = insert_item
        next_empty_list = linked_list[emptyList].nextNode
        linked_list[emptyList].nextNode = -1
        empty_list = next_empty_list
        return True, empty_list
    else:
        return False


print(addNode(linkedList, start_pointer=0))
outputNodes(linkedList, start_pointer=0)

