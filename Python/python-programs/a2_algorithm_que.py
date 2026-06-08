
from operator import le


def jump_jump(n):
    if n in (1, 2):
        return n
    return jump_jump(n - 1) + jump_jump(n - 2)


print(jump_jump(8))


def difference(numbers):
    result = []
    for i in range(0, len(numbers) - 1):
        carry = numbers[i + 1] - numbers[i]
        result.append(carry)
    return result


# print(difference([1, 2, 5, 3]))


def peakValue(numbers):
    result = []
    for i in range(0, len(numbers)):
        if i == 0:
            if numbers[0] > numbers[1]:
                result.append(numbers[0])
        elif i == (len(numbers) - 1):
            if numbers[-1] > numbers[i - 1]:
                result.append(numbers[-1])
        else:
            if numbers[i - 1] < numbers[i] > numbers[i + 1]:
                result.append(numbers[i])
    return result


# print(peakValue([1, 5, 2, 6, 1]))
#
# list = [1, 5, 2, 6, 1]


def reverseStr_2(str):
    word_list = []
    last = 0
    isWord = False
    result = ''
    for i in range(len(str)):
        if i < (len(str) - 1):
            if str[i] != ' ':
                isWord = True
            elif str[i] == ' ' and isWord is True:
                isWord = False
                word_list.append(str[last:i]), word_list.append(str[i])
                last = i + 1
            elif str[i] == ' ' and isWord is False:
                word_list.append(str[i])
                last = i
                last += 1
                isWord = False
        elif str[i] != ' ':
            word_list.append(str[last:])
        else:
            word_list.append(str[last:i]), word_list.append(str[i])
    for n in word_list[::-1]:
        result += n
    return word_list, result, last


# print(reverseStr_2('the sky is blue  '))


# Mr Rock sample answer
def reverseStr_rock(str):
    word_list = []
    tem = ""
    result = ''
    for i in range(len(str)):
        print(tem)
        if str[i] == ' ':
            if tem == "" or tem[0] == " ":
                tem += str[i]
            else:
                # 添加文字
                word_list.append(tem)
                tem = str[i]
        else:
            if tem == "" or tem[0] != " ":
                tem += str[i]
            else:
                # 添加空格
                word_list.append(tem)
                tem = str[i]
    word_list.append(tem)

    for n in word_list[::-1]:
        result = result + n
    return word_list, result


# print(reverseStr_rock('the sky is   blue '))


def reversion(word):
    list_1 = word.split(' ')
    list_2 = []
    result = ''
    for i in range(len(list_1)):
        if list_1[i] != '':
            list_2.append(list_1[i])
            list_2.append(' ')
        else:
            list_2.append(' ')
    list_2.pop(-1)
    for n in list_2[::-1]:
        result += n

    return list_2, result


# print(reversion('the   sky  is   blue'))

def jacky_split(a_string, target):
    temp_str = []
    len_string = len(a_string)
    len_target = len(target)
    for i in range(len_string):
        index = a_string.find(target)
        print(index)
        if index == -1:
            temp_str.append(a_string)
            return temp_str
        else:
            temp_str.append(a_string[:index])
            a_string = a_string[index + len_target:]


# print(jacky_split('the   sky is  blue', 'bl'))
