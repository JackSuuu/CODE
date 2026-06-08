

# 给定 3 个正整数 n, b 和 s, 生成以给定进制内的数字 s 开始的接下来 n 个 b 进制数字。
# 我们确保进制介于 2 和 16 之间（2 <= x <= 16）并且 s 是一个 b 进制的有效数字。
# 找出生成数字的各个数位上的所以数字，并打印输出出现频率最高的数字对应出现总次数的十进制数。

# 解题思路
# 1. 生成从 s 开始的 base 进制数，number 循环
#   - 模拟进制相加
#   - 添加生成数进数组
# 2. 从生成数中查找出现次数最多的数字
#   - 从 0 ～ base 开始逐个查找，将数字添加，输出最大值
#   - 设置一个 highest 变量，使用 each highest 遍历所有数组

def highNumAppear(number: int, base: int, s: str):
    # 进模拟进制相加
    num_arr = [s]
    num_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    base_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    for i in range(number, -1, -1):
        # 分开小于和大于10的数
        if s[-1] in num_dict.keys():
            add_sum = num_dict[s[-1]] + 1
            if add_sum >= base:
                s[-1] = '0'
                carry = True
                while carry:
                    pass
            else:
                s[-1] = base_dict[add_sum]
        else:
            add_sum = int(s[-1]) + 1
            if add_sum >= base:
                s[-1] = '0'
                carry = True
                while carry:
                    pass
            else:
                s[-1] = base_dict[add_sum]
        num_arr.append(s)
    # 从生成数中查找出现次数最多的数字
    highest = 0
    each_highest = 0
    for i in range(base):
        for each in num_arr:
            if i >= 10:
                pass
            else:
                if str(i) in each:
                    for e in each:
                        if str(i) == e:
                            each_highest += 1
        if each_highest > highest:
            highest = each_highest

    return highest


print(highNumAppear(15, 2, '1111011'))


