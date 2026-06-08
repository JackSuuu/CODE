
# 编写一个函数来查找字符串数组中的最长公共前缀
# 如果不存在公共前缀，返回空字符串 ""

test_1 = ["flower", "flow", "flight"]
test_2 = ["dog", "racecar", "car"]
test_3 = [""]


def longestCommonPrefix(strs: list[str]):
    prefix = ''
    same = True
    while same and ('' not in strs):
        first_char = strs[0][0]
        for i in range(len(strs)):
            if strs[i][0] != first_char:
                same = False
                break
            else:
                strs[i] = strs[i][1:]
        if same:
            prefix += first_char
    return prefix


print(longestCommonPrefix(test_1))
