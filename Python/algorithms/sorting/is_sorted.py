
def is_sorted(a_list):
    if len(a_list) == 1:
        return True  # Base case
    else:
        return a_list[0] <= a_list[1] and is_sorted(a_list[1:])


a = [1, 3, 4, 5, 9]
b = [0, 1, 2, 6, 3]
print(is_sorted(a))
print(is_sorted(b))

print({(True and True) and True} and False)
