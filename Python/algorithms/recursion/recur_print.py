
def print_for(n):
    for i in range(n):
        print(i)
        
def recur_for(n):
    if n == 5:
        print(5)
    else:
        print(n)
        recur_for(n+1)
        
# print_for(5)
recur_for(1)
