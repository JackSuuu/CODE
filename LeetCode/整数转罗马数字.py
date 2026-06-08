

def intToRoman(num: int):
    output = ''
    while num > 0:
        if len(str(num)) == 4:
            output += 'M' * int(str(num)[0])
            num -= 1000 * int(str(num)[0])
        elif len(str(num)) == 3:
            if num >= 500:
                if num >= 900:
                    output += 'CM'
                    num -= 900
                else:
                    output += 'D'
                    num -= 500
            else:
                if num >= 400:
                    output += 'CD'
                    num -= 400
                else:
                    output += 'C'
                    num -= 100
        elif len(str(num)) == 2:
            if num >= 50:
                if num >= 90:
                    output += 'XC'
                    num -= 90
                else:
                    output += 'L'
                    num -= 50
            else:
                if num >= 40:
                    output += 'XL'
                    num -= 40
                else:
                    output += 'X'
                    num -= 10
        else:
            if num >= 5:
                if num >= 9:
                    output += 'IX'
                    num -= 9
                else:
                    output += 'V'
                    num -= 5
            else:
                if num >= 4:
                    output += 'IV'
                    num -= 4
                else:
                    output += 'I'
                    num -= 1
    return output


print(intToRoman(4))


def intToRoman(num: int) -> str:
    convert = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
               10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    res = ''
    for c in convert:
        while num >= c:
            res += convert[c]
            num -= c
    return res
