

s = ["e", "m", "a", "s", "A"]


def reverse_string():
    global s
    front_pointer = 0
    tail_pointer = len(s) - 1
    while front_pointer < tail_pointer:
        s[front_pointer], s[tail_pointer] = s[tail_pointer], s[front_pointer]
        front_pointer += 1
        tail_pointer -= 1


reverse_string()
print(s)
