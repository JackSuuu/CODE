def removeDuplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove duplicate
        else:
            stack.append(char)
    return ''.join(stack)

# Test: "abbaca" -> "ca"
print(removeDuplicates(s="abbaca"))