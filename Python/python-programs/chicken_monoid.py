

ns = set()
for i in range(8):
    for j in range(8):
        for k in range(8):
            n = 6 * i + 9 * j + 20 * k
            if n <= 48:
                ns.add(n)

comp = set(range(48)) - ns
print(comp)