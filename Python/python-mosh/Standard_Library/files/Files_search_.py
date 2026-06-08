from pathlib import Path


def find(que):
    rep1 = que.replace("qp", "ms")
    rep2 = rep1.replace("9618.qus", "9618.ans")
    return rep2

def remove(list):
    for i in range(len(list)):
        str1 = list[i]
        list[i] = str1[11, 94]

file_list = []

paths = Path('/Users/jack/Desktop/Python/Python_project/Examable/搜题题库/9618.qus')
for path in paths.iterdir():
    if path.is_file():
        file_list.append(path)

print(remove(file_list))





