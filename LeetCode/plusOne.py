
def plusOne(s: str):
    carry = True
    s = list(s)

    for i in range(len(s)-1, -1, -1):
        print(s[i])

        if carry:
            if s[i] == "1":
                s[i] = "0"
            else:
                s[i] = "1"
            if 1 + int(s[i]) == 2:
                carry = False
        else:
            break
    
    s = "".join(s)

    return "1" + s if carry else s

print(plusOne("1111"))