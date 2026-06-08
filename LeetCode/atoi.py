import re
# 函数 myAtoi(string s) 的算法如下：
# 读入字符串并丢弃无用的前导空格
#
# 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。
# 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
#
# 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。
# 字符串的其余部分将被忽略。
#
# 将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。
# 如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
# 小于 −2^31 的整数应该被固定为 −23^1 ，大于 2^31 − 1 的整数应该被固定为 2^31 − 1。

test = '   +0 123'
test2 = '+-12'  # 返回12
test3 = ' -0012a42'  # 返回12


def my_atoi(s: str):
    is_positive = True
    result = ''
    number_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # 极端用例
    if s == '':
        return 0

    # 读入字符串并丢弃无用的前导空格
    front_space = True
    for i in range(len(s)):
        if s[i] != ' ':
            result += s[i]
            front_space = False
        else:
            if not front_space:
                result += s[i]

    # 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。
    for each in result:
        if each == '+':
            is_positive = True
            result = result[1:]
            break
        elif each == '-':
            is_positive = False
            result = result[1:]
            break
        else:
            break

    # 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。
    for i in range(len(result)):
        if result[i] not in number_array:
            result = result[:i]
            break

    # 将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。
    # 如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
    if result == '':
        return 0
    else:
        if is_positive:
            if int(result) > (2**31) - 1:
                return (2**31) - 1
            else:
                return int(result)
        else:
            if -int(result) < -(2**31):
                return - 2**31
            else:
                return -int(result)


print(my_atoi(test3))


# 正则表达式解法
def Atoi(s: str):
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    s = str.lstrip(' ')  # 清除左边多余的空格
    num_re = re.compile(r'^[\+\-]?\d+')  # 设置正则规则
    num = num_re.findall(s)   # 查找匹配的内容
    num = int(*num)  # 由于返回的是个列表，解包并且转换成整数
    return max(min(num, INT_MAX), INT_MIN)  # 返回值


print(Atoi(test3))
