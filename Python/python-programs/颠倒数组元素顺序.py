
a = [1, 2, 3, 4, 5, 6, 7, 8]
N = len(a)

for i in range(int(N/2)):
    temp = a[i]
    a[i] = a[N-1-i]
    a[N-i-1] = temp

print(a)
