
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/
# 1. 将所以无重复字符的子串提取出来
# 2. 查找最长的子串
s1 = "pwwkew"
s2 = "su"


def lengthOfLongestSubstring(s: str):
    s_arr = []
    max_value = 0
    tem = ''
    for i in range(len(s)):
        if s[i] in tem:
            s_arr.append(tem)
            if tem[-1] == s[i]:
                tem = s[i]
            else:
                pos = tem.find(s[i])
                tem = tem[pos+1:] + s[i]
        else:
            tem += s[i]
    s_arr.append(tem)
    # 获取最大值
    for sub in s_arr:
        if len(sub) > max_value:
            max_value = len(sub)

    return s_arr, max_value


print(lengthOfLongestSubstring(s1))
