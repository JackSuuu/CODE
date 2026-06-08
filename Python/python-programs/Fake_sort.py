import itertools 

list1 = []

x = input("Enter the number you need to rearrange:")


def splitNum():
    b = x.split('/')
    list1.append(b)


splitNum()
list1 = list(itertools.chain.from_iterable(list1))
out = list(map(float, list1)) 

out.sort(reverse=True)
print(out)

