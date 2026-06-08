digits = [1, 9, 9, 9]


def plusOne_lazy(digits):
    each = ''
    number = ''
    result = []
    for i in range(len(digits)):
        each = digits[i]
        number += str(each)
    number = int(number)
    number += 1
    number = str(number)
    for num in number:
        result.append(str(num))
    return result, number


def plusOne(digits):
    is_9 = True
    i = len(digits) - 1
    while i >= 0:
        if digits[i] == 9:
            if i == 0 and is_9 is True:
                digits[i] = 1
                digits.append(0)
                is_9 = False
            if i == (len(digits) - 1) or is_9 is True:
                digits[i] = 0
                is_9 = True
        else:
            if i == (len(digits) - 1) or is_9 is True:
                digits[i] += 1
                is_9 = False
        i -= 1
    return digits


# print(plusOne_lazy(digits))
print(plusOne(digits))
