N = 5
first_arr = [1, 2, 2, 2, 1]
secon_arr = [1, 5, 3, 3, 4]

# 0 2 3 0 4 5
# 3 0 1 1 3


def AcCow(number, arr_1: list, arr_2: list):
    diff_arr = []
    count = 0
    max_i = number

    # 生成 diff_arr
    for i in range(number):
        diff = arr_2[i] - arr_1[i]
        diff_arr.append(diff)

    while True:
        max_num = float('-inf')

        for n in range(number):
            if diff_arr[n] > max_num and diff_arr[n] != 0:
                max_num = diff_arr[n]

        for k in range(number):
            if diff_arr[k] != 0 and max_num > 0:
                diff_arr[k] -= max_num
            elif diff_arr[k] != 0 and max_num < 0:
                diff_arr[k] -= max_num

        if max_num != float('-inf'):
            if max_num > 0:
                count += max_num
            elif max_num < 0:
                count -= max_num
        else:
            break

    return count


print(AcCow(N, first_arr, secon_arr))
