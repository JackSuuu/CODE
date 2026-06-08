import random

# 数组所有数之和问题
a = [random.randint(1, 10) for i in range(10)]
print(a)


# 循环解决方案
def arr_sum(arr):
    s = 0
    for each in arr:
        s += each
    return s


# print(arr_sum(a))


# 分而治之解决方案
def arr_sum_curr(arr, res):
    if not arr:
        return res
    res += arr[0]
    return arr_sum_curr(arr[1:], res)


# print(arr_sum_curr(a, 0))


# 《算法图解》解决方案
def arr_sum_curr_book(lis):
    if not lis:
        return 0  # 0 + f([6]) + f([4]) + f([2])
    return lis[0] + arr_sum_curr_book(lis[1:])


# print(arr_sum_curr_book(a))

def find_max(arr: list):
    if len(arr) == 1:
        return arr.pop()
    if arr[0] > arr[1]:
        arr.pop(1)
        return find_max(arr)
    else:
        arr.pop(0)
        return find_max(arr)


print(f"The biggest number is: {find_max(a)}")

