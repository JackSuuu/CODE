

st = "Hello World    "
a = "only"


def length_of_last_word(s: str):
    count = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] != " ":
            count += 1
        else:
            if count != 0:
                return count
    return count


print(length_of_last_word(a))
