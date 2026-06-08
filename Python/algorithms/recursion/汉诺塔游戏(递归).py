

def hanoi(n, x, y, z):
    if n == 1:
        print(f'{x} --> {z}')
    else:
        hanoi(n-1, x, z, y)  # 将 n-1 个盘子从 x 移动到 y 上
        print(f'{x} --> {z}')  # 将最底下的最后一个盘子从 x 移动到 y 上
        hanoi(n-1, y, x, z)  # 将 y 上的 n-1 个盘子移动到 z 上


n = int(input('请输入汉诺塔的层数: '))

hanoi(n, 'A', 'B', 'C')

