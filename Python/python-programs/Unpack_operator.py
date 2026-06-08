numbers = [1, 2, 3]
print(*numbers)

values = list(range(5))
values = [*range(5), *"Hello"]
print(values)

first = [1,2]
second = [3]
values = [*first, "a", *second]
print(values)

dic1 = {"x": 1}
dic2 = {"x": 10, "y":2}
combined = {**dic1, **dic2, "z":1}
print(combined)