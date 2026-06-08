
def isPlaindrome(str):
    i = len(str) - 1
    Nstr = ''
    while i >= 0:
        Nstr = Nstr + str[i]
        i -= 1
    if Nstr == str:
        return True
    else:
        return False


str1 = "1234321"
print(isPlaindrome(str1))


def getMax(list):
    max = list[0]
    for each_num in list:
        if each_num > max:
            max = each_num
    return max


list = [-78, -4, -8, -7, -3]
print(getMax(list))
