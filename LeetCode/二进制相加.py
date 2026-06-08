
a_num = '1'
b_num = '111'
# output 1, 0, 0, 0


def binary_plus(a, b):
    # 考虑两个 binary value 长度关系
    carry = 0
    len_a = len(a)
    len_b = len(b)
    result = ''
    # 选择 base 和 divider
    if len_a > len_b:
        base, divider = a, b
        divider = '0' * abs(len_a - len_b) + divider
    else:
        base, divider = b, a
        divider = '0' * abs(len_a - len_b) + divider
    # 逆序遍历
    for i in range(len(base)-1, -1, -1):
        sum = int(base[i]) + int(divider[i]) + carry
        if sum == 0 or sum == 2:
            result = '0' + result
            carry = 0
        else:
            result = '1' + result
            carry = 0
        if sum == 2 or sum == 3:
            carry = 1
    if carry == 1:
        return '1' + result
    else:
        return result


print(binary_plus(a_num, b_num))
