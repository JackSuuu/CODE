x = 135797531


def isPalindrome(x):
    x_str = str(x)
    if x_str[::-1] == x_str:
        return True
    else:
        return False


# using round()
# 121 == 121 no str()
# 取余操作回文数
def isPalindrome_No_str(x):
    min_v = 1
    div_v = 10
    num_arr = []
    origin_x = x
    convert_x = 0
    if x < 0:
        return False
    else:
        while x > 0:
            count = 0
            while x % div_v != 0:
                x -= min_v
                count += 1
            num_arr.append(count)
            min_v *= 10
            div_v *= 10
        min_v /= 10
        for i in range(len(num_arr)):
            convert_x += (num_arr[i] * min_v)
            min_v /= 10
        if origin_x == convert_x:
            return True
        else:
            return False


print(isPalindrome_No_str(x))





