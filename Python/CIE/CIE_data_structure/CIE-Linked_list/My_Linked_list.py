
# A --> 3
# D --> 1
# B --> 2
# C --> -1
my_linked_list = ["A", "B", "C", "D"]  # linked_list index = pointer position
linked_list_pointer = [3, 2, -1, 1]


def search(item):
    global my_linked_list, linked_list_pointer
    list_item = my_linked_list[0]
    next_pointer = linked_list_pointer[0]
    while next_pointer != -1:
        if list_item != item:
            next_pointer = linked_list_pointer[my_linked_list.index(list_item)]
            print(f'{list_item} --> {next_pointer}')
            list_item = my_linked_list[next_pointer]
        else:
            return my_linked_list.index(list_item)
    return -1


print(search("C"))


def addLast(item):
    global my_linked_list, linked_list_pointer
    my_linked_list.append(item)
    last_pointer_pos = linked_list_pointer.index(-1)
    linked_list_pointer[last_pointer_pos] = my_linked_list.index(item)
    linked_list_pointer.append(-1)


print(addLast("E"))
print(my_linked_list, linked_list_pointer)

