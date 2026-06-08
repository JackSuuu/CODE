

# f(x-1, y+2) + 3 if x > y
# 2*f(x+1, y-1) - 5 if x < y
# x*x+y if x = y

def re_fun(x, y):
    if x == y:
        return x * x + y
    elif x > y:
        return re_fun(x - 1, y + 2) + 3
    else:
        return x * re_fun(x+1, y-1) - 5


print(re_fun(12, 7))
