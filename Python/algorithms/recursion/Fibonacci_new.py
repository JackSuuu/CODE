
# get any position Fibonacci number
# 0 1 1 2 3 5 8 13 21...
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# print(fib(6))


# The sum of Fibonacci Series
def sum_fib(level):
    s = 0
    for i in range(level):
        s += fib(i)
    return s


# print(sum_fib(5))


def print_curr(n):
    if n == 0:
        return
    print(n)
    return print_curr(n-1)


print_curr(10)
