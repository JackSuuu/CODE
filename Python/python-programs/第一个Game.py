# 用python设计第一个游戏

import random

counts = 3
answer = random.randint(1, 10)

while counts > 0:
    temp = input("不妨猜一下我心中想的是哪个数字：")
    guess = int(temp)

    if guess == answer:
        print("你是我心中的蛔虫吗？！")
        print("猜中了也没奖励")
        break
    else:
        if guess < answer:
            print("小啦！")
        else:
            print("大啦！")
        counts = counts - 1
         
print("Game is over, stop playing ^-^")

    
