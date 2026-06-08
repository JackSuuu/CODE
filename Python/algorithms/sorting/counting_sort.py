

def counting_sort(arr):
    # 寻找待排序数组的最大值和最小值
    min_val = min(arr)
    max_val = max(arr)

    # 创建计数数组并初始化为0
    count = [0] * (max_val - min_val + 1)

    # 计算元素频率
    for num in arr:
        # 用 num - min_val 确认元素的偏移量
        count[num - min_val] += 1

    # 计算累积频率
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 生成排序数组
    sorted_arr = [0] * len(arr)

    # 排序过程
    for num in reversed(arr):
        index = count[num - min_val] - 1
        sorted_arr[index] = num
        count[num - min_val] -= 1

    return sorted_arr


arr = [4, 2, 3, 4, 1]
res = counting_sort(arr)
print(res)
