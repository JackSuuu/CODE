test = -2147483412


def reverse(x: int):
    tem = ''
    flag = False
    str_x = str(x)

    for i in range(len(str_x)-1, -1, -1):
        if str_x[i] != 0:
            flag = True
            tem += str_x[i]
        else:
            if not flag:
                tem += str_x[i]

    if x < 0:
        if - int(tem[:-1]) > -2**31:
            return - int(tem[:-1])
        else:
            return 0
    elif x > 0:
        if int(tem) < 2**31:
            return int(tem)
        else:
            return 0
    else:
        return 0


print(reverse(test))

