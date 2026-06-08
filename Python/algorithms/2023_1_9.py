# Recursion: a method that call itself to solve problem recursively
# An equally powerful substitute for iteration (loops)
# Particularly well-suited to solving certain types of problems


def tellingStory(i):
    if i == 1:  # stop condition
        print("Once upon a time there was a mountain...")
        return 1
    else:
        return tellingStory(i - 1)


# tellingStory(5)


# 电影院排数：问前面一个人，前面一个人再问前面一个人，一直往前问，直到第1排
# 先递进，然后回溯
def position(n):
    if n == 1:  # stop condition
        return 1  # base case: Unwinding can occur once the base case is reached
    return position(n - 1) + 1  # Recursive call (general/recursive case)


# print(position(4))


# Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


# result = 'o' + R('Hell')
# R('Hell') = 'l' + R('Hel')
# R('Hel') = 'l' + R('He')
# R('He') = 'e' + R('H')
# R('H') = 'H'
def reverse(str1):
    if len(str1) == 1:
        result = str1
    else:
        result = str1[-1] + reverse(str1[0: -1])
    return result


# print(reverse("Hello"))
