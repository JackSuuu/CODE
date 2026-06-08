import random
import cmath

arr = [random.randint(1, 50) for i in range(10)]


def insertion_descending(score: list):
    for student in range(len(score)):
        tem_score = score[student]
        curr_index = student
        while tem_score > score[curr_index - 1] and curr_index > 0:
            score[curr_index] = score[curr_index - 1]
            curr_index -= 1
        score[curr_index] = tem_score
    return score


# print(f"The score array: {insertion_descending(arr)}")


# 定义两个复数
z1 = 3 + 4j
z2 = 5 - 2j

# 将复数转换为极坐标形式
r1, theta1 = cmath.polar(z1)
r2, theta2 = cmath.polar(z2)

# 计算乘积的模长和辐角
r = r1 * r2
theta = theta1 + theta2

# 将乘积转换为直角坐标形式
z = cmath.rect(r, theta)

print(z)  # 输出结果为 (-2+23j)

