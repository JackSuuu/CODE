

# 99乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(j, "*", i, "=", j * i, end=" ")
#         j += 1
#     print()
#     i += 1

def Jack_9x9():
    x = 0
    for i in range(1, 10):
        for n in range(1, i + 1):
            x = i * n
            print(i, ' x ', n, ' = ', x, end='\t')
        print('')


Jack_9x9()