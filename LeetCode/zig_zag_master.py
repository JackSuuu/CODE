
def convert(s: str, numRows: int) -> str:
    if numRows < 2:
        return s
    res = ["" for _ in range(numRows)]
    i, flag = 0, -1
    for c in s:
        res[i] += c
        if i == 0 or i == numRows - 1:
            flag = -flag
        i += flag

    return "".join(res)


s = "ABCDEFGHIJK"
# A   E   I
# B D F H J
# C   G   K

print(convert(s, 1))
