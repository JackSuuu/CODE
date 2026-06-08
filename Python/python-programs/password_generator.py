import random

a_list = []


# My young way to implement a password generator
def Getstate():
    a = random.randint(0, 100)
    if a >= 10:
        c = chr(a)
        list.append(c)
    else:
        list.append(str(a))


count = 0
while count <= 15:
    Getstate()
    count += 1

random.shuffle(a_list)
# print(''.join(a_list))


# My new way after I studied programming a year
def passGene():
    # character = 0
    password = ''
    length = int(input("Please input the length of password you desire: "))
    for i in range(length):
        character = random.randint(0, 1000)
        character = chr(character)
        password += character
    return password


print(passGene())



    
