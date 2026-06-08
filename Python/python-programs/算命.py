import random


def fate():
    brithday_date = input("请输入你的出生日期(year:month:day): ")
    date_arr = brithday_date.split(':')
    print("your brithday date is: ", date_arr)

    lucky_number = int(input("请输入你的幸运数字, 如果没有请输入 0："))
    desire_date = int(input("请输入想要生成的月份："))
    if lucky_number == 0:
        lucky_number = random.randint(1, 1000)

    random_num = random.randint(1, lucky_number)

    sum = 0
    for i in range(len(date_arr)):
        sum += int(date_arr[i])

    result = 0
    for i in range(0, 1000):
        sum += 1
        result = round(sum/random_num)

    while result > 30:
        result = round(result/random_num)

    return f"您在{desire_date}月的幸运日期是，{desire_date}月{result}日"


print(fate())

