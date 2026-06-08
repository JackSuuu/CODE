def intToRoman(num: int) -> str:
    rom_tab = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    sub_tab = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

    s_num = str(num)
    res = ""

    while s_num != "0":
        n = s_num[0]
        print(n, num, res)
        if int(n) not in (4, 9):
            for key, val in reversed(rom_tab.items()):
                if num - val >= 0:
                    res += key
                    num -= val
                    s_num = str(num)
                    break
        else:
            for key, val in reversed(sub_tab.items()):
                if num - val >= 0:
                    res += key
                    num -= val
                    s_num = str(num)
                    break
    
    return res

print(intToRoman(1994))