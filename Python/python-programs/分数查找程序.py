
# 分数查找程序
score = input("Please enter your score")
score = int(score)

if 0 <= score <= 60:
    print("You score is counted as D")
elif 60 <= score <= 80:
    print("You score is counted as C")
elif 80 <= score <= 90:
    print("You score is counted as B")
elif 90 <= score <= 99:
    print("You score is counted as A")
elif score == 100:
    print("Well done!! You score are legendary")
elif score == 101:
    print("A")
else:
    print("Please enter the number between 0 to 100")
