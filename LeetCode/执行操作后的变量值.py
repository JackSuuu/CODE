# 存在一种仅支持 4 种操作和 1 个变量 X 的编程语言：
# ++X 和 X++ 使变量 X 的值 加 1
# --X 和 X-- 使变量 X 的值 减 1

operation_list = ["--X", "X++", "X++"]


def finalValueAfterOperations(operations: list[str]):
    x = 0
    for each in operations:
        if each[0] == '+' or each[-1] == '+':
            x += 1
        else:
            x -= 1
    return x


print(finalValueAfterOperations(operation_list))
