D = [9, 9]
n = 2

def Inc():
    i = 0
    while i < n and D[i] == 9:
        D[i] = 0
        i = i + 1
    if i < n:
        D[i] = D[i] + 1

Inc()
print(D)