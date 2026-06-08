import random
import string

print('\n')
print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print("".join(random.choices(string.ascii_letters + string.digits, k=11)))

numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)

print(string.ascii_letters)
print(string.digits)
print('\n')
