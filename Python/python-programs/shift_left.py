

array = [8, 7, 1, 2, 3]


def insert_last(item):
    global array
    array.append(item)


def delete_first():
    global array
    delete_item = array[0]
    array = array[1:]
    return delete_item


# Recursive Version
def shift_left(d, k):
    if k == 0:
        return "Done"
    insert_last(delete_first())
    return shift_left(d, k-1)


shift_left(array, 3)
print(array)
