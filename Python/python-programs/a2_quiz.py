
def getMax3(num1, num2, num3):
    nums = []
    nums.append(num1)
    nums.append(num2)
    nums.append(num3)
    max_num = nums[0]
    for each in nums:
        if each > max_num:
            max_num = each
    return max_num


def getMax3_2(num1, num2, num3):
    max_num = num1
    if max_num < num2:
        max_num = num2
    if max_num < num3:
        max_num = num3
    return max_num


# print(getMax3(1, 3, 2))
# print(getMax3_2(1, 3, 2))


def getEven(list):
    count = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            count += 1
    return count

# list = [1, 2, 3]
# print(getEven(list))

# 3、 写一个function，求出考试分数对应的字母等级，输入参数为考试分数，返回字母等级
def grade(mark):
    boundry = [29, 39, 59, 69, 79, 89, 100]
    key = '0'
    dic = {'0': 'Unbelieveable',
           '1': 'E',
           '2': 'D',
           '3': 'C',
           '4': 'B',
           '5': 'A',
           '6': 'A*'}
    for i in range(0, len(boundry)):
        if int(mark) <= boundry[i]:
            print(i)
            key = str(i)
            print(key)
            break
    return dic[key]


# print(grade(29))

# 4、 用For循环嵌套的方式打印出99乘法表
def table():
    for i in range(0, 10):
        for j in range(1, i + 1):
            print(i, 'x', j, '=', i * j, end="  ")
        print()


# table()

# 5、 写一个function，输入参数为一个整数X，返回为 1！+2！+3！+4！+ ...+ X! 阶乘的和
# 改为 for 循环
def factorial(X):
    total = 0
    for i in range(1, X+1):
        temp = 1
        for j in range(1, i+1):
            temp = temp * j
        total = total + temp
    return total


print(factorial(5))


# 附加题：
# 写一个function，输入参数为两个字符串str和target，返回True或False，例如：
# 如果str = “ajciedwok” target = "jack", 则返回结果为True，因为str中包含了target字符串中的每一个字符。
# 否则返回False。

str = "ajciedwok"
target = "jack"

def check_str(str, target):
    count = 0
    standard = len(target)
    for i in target:
        for j in str:
            if i == j:
                count += 1
    if count == standard:
        return True
    else:
        return False


def findTarget(str, target):
    for i in range(0, len(target)):
        flag = 0
        for j in range(0, len(str)):
            if target[i] == str[j]:
                flag = 1
        if flag == 0:
            return False
    return True


print(check_str(str, target))
print(findTarget(str, target))

