n = int(input("Please input the value of factorial:"))


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(n))

