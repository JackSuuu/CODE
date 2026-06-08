# 除去多余空格

sentence = "this   is  a  sentence"
# this is a sentence


def removeSpace(strA):
    flag = False
    strB = ''
    for each in sentence:
        if each != ' ':
            strB += each
            flag = True
        else:
            if flag == True:
                strB += ' '
                flag = False
    if strB[-1] == ' ':
        strB = strB[0:-1]

    return strB


print(removeSpace(sentence))
