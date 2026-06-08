
# From p / 2 + n to p
# 1 + (p//n)
n = 3
p = 16

def nth_element(n, p):
    return [num for num in range(int(p/2), p+1, n)]

# print([i for i in range(8, 16, 3)])
# print(16 // 2)

print(nth_element(5, 15))