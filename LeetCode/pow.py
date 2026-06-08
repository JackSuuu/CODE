

def my_pow(x: float, n: int):
    if n == 0:
        return 1
    elif n < 0:
        x = 1 / x
        n = - n
    res = x
    for i in range(1, n):
        res *= x
    return res


print(my_pow(2.0, -2))
