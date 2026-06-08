
# base 10 t0 base 2
cnm = []
temp = input("请输入十进制代码：")
num = int(temp)
while num > 0:
    x = num
    x = x % 2
    cnm.insert(len(cnm), x)
    num = num // 2

cnm.reverse()
print(cnm)
