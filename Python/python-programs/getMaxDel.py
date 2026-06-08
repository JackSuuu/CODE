def getMaxDeletions(s):
    # use a stack to hold either U or D, R or L
    # if a corresponding element matches: delete two total int
    u_stack = []
    r_stack = []
    total = 0
    
    for char in s:
        if char == 'U' and u_stack and u_stack[0] == 'D':
            u_stack.clear()
            total += 2
        elif char == 'D' and u_stack and u_stack[0] == 'U':
            u_stack.clear()
            total += 2
        elif char == 'L' and r_stack and r_stack[0] == 'R':
            r_stack.clear()
            total += 2
        elif char == 'R' and r_stack and r_stack[0] == 'L':
            r_stack.clear()
            total += 2
        else:
            if char in ('U', 'D'):
                u_stack.append(char)
            else:
                r_stack.append(char)
            
    return total

print(getMaxDeletions("ULUDUULLUD"))