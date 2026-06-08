import re
# 正则表达式

a = re.match('test', 'testasdtest')
print(a)
print(a.group())
print(a.span())
print(re.match('test', 'atestasdtest'))

a = re.match('..', 'testasdtest')
print(a.group())  # 输出te
b = re.match('ab.', 'testasdtest')
print(b)

a = re.match('\d\d', '23es12testasdtest')
print(a, '\n')

print(re.match('\w', '23es 12testasdtest'))   # 返回none
print(re.match('\w\w\w', 'aA_3es 12testasdtest'))   # 返回none
print(re.match('\w\w\w', '\n12testasdtest'), '\n')   # 返回none

a = re.match('..', 'testasdtest')
print(a.group())   # 输出te
a = re.match('.*', 'testasdtest')
print(a.group())   # 全部输出

a = re.match(r'<h1>(.*)<h1>', '<h1>你好啊<h1>')
print(a.group())    # 输出匹配的字符
print(a.groups())   # 会将()中的内容会作为一个元组字符装在元组中
print('\n')

b = re.match(r'<h1>(.*)(<h1>)', '<h1>你好啊<h1>')
print(b.groups())  # 有两括号就分为两个元组元素
print(b.group(0))  # group中默认是0
print(b.group(1))  # 你好啊
print(b.group(2))  # h1
print('\n')

a = """aaatestaa     
aaaa123"""
print(re.findall(r'test.*123', a))
print(re.findall(r'test.*123', a, re.S), '\n')

s = "itcase,java:php-php3;html"
print(re.split(r",", s))           # 以,号进行分割
print(re.split(r",|:|-|;", s))     # 以,或者：或者-或者;进行分割
print(re.split(r",|:|-|%", s))    # 找不到的分隔符就忽略
