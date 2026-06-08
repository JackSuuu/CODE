from re import X


def isUnique(astr):
    len_str = len(astr)
    for i in range(0, len_str):
        for n in range((i + 1), len_str):
            if astr[i] == astr[n]:
                print(astr[i])
                print(astr[n])
                return False
    return True


print(isUnique("Leetcode"))
print(isUnique("abc"))
