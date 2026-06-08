
def convert(s: str, numRows: int) -> str:
    cou = 0
    tem = ''
    skip = - numRows + 2
    row_lis = []
    mid_lis = []
    result = ''
    for i in range(len(s)):
        if cou == numRows:
            cou = skip
            mid_lis.append(s[i:(i + numRows - 2)])
            row_lis.append(tem)
            tem = ''
        if cou >= 0:
            tem += s[i]
        cou += 1
    row_lis.append(tem)
    cou = 0
    # while cou <= numRows:
    #     for n in row_lis:
    #         result += n[cou]
    #         if cou == numRows:

    return row_lis, mid_lis, result


def convert_new(s: str, numRows: int) -> str:
    n = 0
    current_row = 0
    result = ''
    end = 2 * (numRows - 1)
    print(end)
    last = 0
    # 中间值初始值肯定是1
    mid_row = 1
    p_value = 1
    if numRows < 2:
        return s
    if numRows > 3:
        p_value = numRows - 2
    while current_row < numRows:
        if mid_row == numRows - 1:
            mid_row = -999
        n = 0
        for i in range(len(s)):
            # 层数条件判读
            if i == current_row or i == (current_row + end * n):
                result += s[i]
                # 设置上一个获取的值
                # 如果 大于 3 层，last 从 +4 开始，下一层递减
                last = i
                # 设置步进值
                n += 1
            if i == (last + 2 * p_value) and current_row == mid_row:
                result += s[i]
        # 设置中间行数列增加
        if current_row != 0:
            mid_row += 1
            # 设置中间特殊值
            p_value -= 1
        # 设置外置 counter
        current_row += 1

    return result


s = 'PAYPALISHIRING'
a = 'A'
alpha = 'ABCDEFGHIJK'
abcd = "ABCD"

# A   E   I
# B D F H J
# C   G   K

# A     G
# B   F H
# C E   I K
# D     J

print(convert_new(alpha, 3))
# print(convert_new(a, 1))
