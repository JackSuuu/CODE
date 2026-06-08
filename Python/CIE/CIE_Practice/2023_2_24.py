import random

# 9608_s18_41-Q2
Item_List = [random.randint(1, 20) for _ in range(20)]
print(Item_List)


def bubble_sort(ItemList: list):
    max_index = 20
    number_items = 19
    for outer in range(0, max_index - 1):
        for inner in range(0, number_items):
            if ItemList[inner] > ItemList[inner + 1]:
                tem = ItemList[inner]
                ItemList[inner] = ItemList[inner + 1]
                ItemList[inner + 1] = tem
        number_items -= 1
    return ItemList


print(bubble_sort(Item_List))
