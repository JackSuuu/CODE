
def reverse(x: int):
    isNeg = False
    if x < 0:
        isNeg = True
        x = abs(x)
    
    revX = 0
    while x > 0:
        digit = x % 10
        revX = revX * 10 + digit
        x //= 10
    
    if isNeg:
        revX = - revX
    
    if revX < -2**31 or revX > 2**31 -1:
        return 0
    
    return revX

print(reverse(123))
