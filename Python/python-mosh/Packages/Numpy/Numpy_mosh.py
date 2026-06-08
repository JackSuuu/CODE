import numpy as np

array = np.array([1, 2, 3])
d_array = np.array([[1, 2, 3], [4, 5, 6]])
print(d_array)
print(d_array.shape)
print(type(array))

c_array = np.zeros((3, 4), dtype=int)
c_array = np.ones((3, 4), dtype=int)
d_array = np.full((3, 4), 5, dtype=int)
e_array = np.random.random((3, 4))
print(c_array)
print(d_array)
print(e_array[0, 0])
print(e_array > 0.2)
print(e_array[array > 0.2]) # return a new array with value only greater than o.2
print(np.sum(array))
print(np.floor(array))
print(np.ceil(array))
print(np.round(array))

first = np.array([1, 2, 3])
second = np.array([1, 2, 3])
print(first + 2)

dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)
