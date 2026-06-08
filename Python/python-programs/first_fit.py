import random

def first_fit(item_list, bin_size):
    bin_list = [0]

    for item in item_list:
        if item <= bin_size - bin_list[0]:
            bin_list[0] += item
        else:
            bin_list.append(item)

    return bin_list

l = [random.randint(1, 10) for _ in range(10)]
bin_size = 4

print(l)
print(first_fit(l, bin_size))
