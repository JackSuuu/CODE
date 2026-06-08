

def jump_staircase(n):
    if n in (1, 2):
        return n
    else:
        return jump_staircase(n - 1) + jump_staircase(n - 2)


print(jump_staircase(8))
