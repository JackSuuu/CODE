
# String Reverse
# a = 'ABC'
# a = 'C' + 'B' + 'A'
# a = CBA
# 拿最后一个，调用最后一个到最前面，再调用最后一个，直到自己等于自己
# str1 = BC | str_cur = A
# str1 = C | str_cur = B
# str1 = '' | str_cur = C
def reverse(str1):
    str_cur = str1[0]
    str1 = str1[1:]
    if str1 == '':  # stop condition / base case
        return str_cur
    return reverse(str1) + str_cur  # recursive call


a = 'ABC'
s = 'emosdnah si kcoR'
print(reverse(a))
print(reverse(s))
