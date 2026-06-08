

def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


# number = int(input('请输入一个正整数：'))
# print("%d 的阶乘是：%d", (number, factorial(number)))


# Factorial in Recursion
def factorial_recur(n: int):
    # Base case
    if n == 1:
        return 1
    return factorial_recur(n - 1) * n


print(factorial_recur(5))
