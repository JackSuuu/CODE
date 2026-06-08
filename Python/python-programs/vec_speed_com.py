import time
import numpy as np

w = np.array([1.0, 2.5, -3.3])
b = 4
x = np.array([10, 20, 30])

def not_vec(w, b, x):
    f = 0
    for j in range(0, len(w)):
        f = f + w[j] * x[j]
    f = f + b

def vec(w, b, x):
    return np.dot(w, x) + b

start = time.time()
vec(w,b,x)
end = time.time()

print(start - end)
