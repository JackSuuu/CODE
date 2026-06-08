
x = 10


def fun(num):
    print(num)
    if num == 0:
        return
    return fun(num - 1) + num


fun(x)


def fun_1():
    count = 0
    while count < 10:
        print(count)
        count += 1
        if count == 5:
            return


# fun_1()
