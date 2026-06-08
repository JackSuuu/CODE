
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：
# 1. 左括号必须用相同类型的右括号闭合。
# 2. 左括号必须以正确的顺序闭合。
# 3. 每个右括号都有一个对应的相同类型的左括号

def isValid(s: str):
    left = ['(', '{', '[']
    right = [')', '}', ']']
    which_bracket = -1
    active = False
    for each in s:
        if each in left:
            active = True
            which_bracket = left.index(each)
        if each in right:
            active = False
            if each == right[which_bracket]:
                which_bracket = -1
            else:
                return False
    if active:
        return False
    else:
        return True


extreme_case = "{[]}"
print(isValid("[]{}{}"))


# ------------------------------------------------------------------
# Using Stack to address the problem
def isValid_Stack(s: str):
    dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
    stack = ['?']
    for c in s:
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c:
            return False
    return len(stack) == 1
