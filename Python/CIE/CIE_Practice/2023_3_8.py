
# 9618_w22_42-Q1
# (a)
Jobs = [[0 for X in range(2)] for Y in range(100)]
NumberOfJobs = 0
print(Jobs)
print("--------------------------------")


# (b)
def Initialise():
    global NumberOfJobs, Jobs
    for i in range(len(Jobs)):
        for n in range(len(Jobs[i])):
            Jobs[i][n] = -1

    NumberOfJobs = 0


Initialise()
print(Jobs)
print("--------------------------------")


# (c)
def AddJob(job_number: int, priority: int):
    global Jobs
    Added = False
    for x in range(len(Jobs)):
        if Added:
            break
        for y in range(len(Jobs[x])):
            if Jobs[x][y] == -1:
                if y == 0:
                    Jobs[x][y] = job_number
                elif y == 1:
                    Jobs[x][y] = priority
                    Added = True
    if Added:
        return "Added"
    else:
        return "Not added"


# (d)
print(AddJob(12, 10))
print(AddJob(526, 9))
print(AddJob(33, 8))
print(AddJob(12, 9))
print(AddJob(78, 1))
print(Jobs)
print("--------------------------------")


test_arr = [[-1, 0], [-1, 4], [-1, 2]]
# (e) InsertionSort() - Procedure
# * Sort data into ascending numerical order of priority
# [0, 3, 2, 1], Jobs = [[-1, 0], [-1, 3], [-1, 2]]
# 1. start with basic insertion sort
# 2. transfer basic to advance


# 从后面往前面插入
def InsertionSort(arr: list):
    for i in range(1, len(arr)):
        pos = i
        curr_num = arr[i]
        if curr_num[1] != -1:
            while arr[pos - 1][1] > curr_num[1] and pos > 0:
                arr[pos] = arr[pos - 1]
                pos -= 1
            arr[pos] = curr_num


InsertionSort(Jobs)
print(Jobs)
print("--------------------------------")


# (f) Print array out in format: 123 priority 1
def PrintArray():
    count = 0
    _priority_ = ''
    _job_number_ = ''
    for Job in Jobs:
        for each in Job:
            if count == 1:
                _priority_ = each
                count = 0
            else:
                _job_number_ = each
                count += 1
        print(f"{_job_number_} priority {_priority_}")


PrintArray()
