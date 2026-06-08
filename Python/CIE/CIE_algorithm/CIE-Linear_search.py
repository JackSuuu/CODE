test_arr = [2, 5, 4, 1, 3]


def linearSearch(alist: list, target):
    pos = []
    for i in range(len(alist)):
        if target == alist[i]:
            pos.append(i)
    if not pos:
        return -1
    else:
        return pos


print(linearSearch(test_arr, 99))
