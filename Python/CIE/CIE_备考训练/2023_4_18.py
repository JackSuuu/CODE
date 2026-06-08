
NumberOfJobs = 100
Jobs = [[0 for X in range(2)] for Y in range(100)]


def Initialise():
    global NumberOfJobs
    NumberOfJobs = 0
    for i in range(len(Jobs)):
        for j in range(2):
            Jobs[i][j] = -1


def AddJob(jobNum: int, priority: int):
    global Jobs
    count = 0
    added = True
    while added:
        if Jobs[count][0] == -1:
            Jobs[count][0] = jobNum
            Jobs[count][1] = priority
            added = False
        count += 1
    if not added:
        print('Added')
    else:
        print('Not added')


Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)
print(Jobs)


# ascending order: small < big


def InsertionSort():
    global Jobs
    for i in range(len(Jobs)):
        curr_job = Jobs[i]
        curr_i = i
        if curr_job[1] == -1:
            break
        while Jobs[curr_i - 1][1] > curr_job[1] and curr_i > 0:
            Jobs[curr_i - 1], Jobs[curr_i] = Jobs[curr_i], Jobs[curr_i - 1]
            curr_i -= 1
        Jobs[curr_i] = curr_job
    return Jobs


def PrintArray():
    global Jobs
    for i in range(len(Jobs)):
        if Jobs[i][0] != -1:
            Job_number = Jobs[i][0]
            Job_priority = Jobs[i][1]
            print(f'{Job_number} priority {Job_priority}')


print(InsertionSort())
PrintArray()


# -----------------------------------------------------------------------------------
class Character:
    def __init__(self, Name: str, XCoordinate: int, YCoordinate: int):
        self.__Name = Name  # PRIVATE STRING
        self.__XCoordinate = XCoordinate  # PRIVATE INTEGER
        self.__YCoordinate = YCoordinate  # PRIVATE INTEGER

    def GetName(self):
        return self.__Name

    def GetX(self):
        return self.__XCoordinate

    def GetY(self):
        return self.__YCoordinate

    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange


character_arr = [Character('', 0, 0) for _ in range(10)]

with open('txt-文件/Characters.txt', 'r') as FILE:
    character_name = FILE.readline().strip().lower()
    count = 0
    while character_name != '':
        x_col = int(FILE.readline().strip())
        y_col = int(FILE.readline().strip())
        character_arr[count] = Character(character_name, x_col, y_col)
        character_name = FILE.readline().strip().lower()
        count += 1

print(character_arr[0].GetName())

find = False
chosen_character_index = 0
while not find:
    input_character_name = 'qui'  # input("Please enter the character name: ")
    for i in range(len(character_arr)):
        if input_character_name == character_arr[i].GetName():
            chosen_character_index = i
            find = True

valid = False
input_direction = ''
while not valid:
    input_direction = 'A'  # input("Please enter a valid move (A, W, S or D): ")
    if input_direction in {'A', 'W', 'S', 'D'}:
        valid = True


if input_direction == 'A':
    character_arr[chosen_character_index].ChangePosition(-1, 0)
if input_direction == 'W':
    character_arr[chosen_character_index].ChangePosition(0, +1)
if input_direction == 'S':
    character_arr[chosen_character_index].ChangePosition(0, -1)
if input_direction == 'S':
    character_arr[chosen_character_index].ChangePosition(+1, 0)

print(f'{character_arr[chosen_character_index].GetName()} has changed coordinates '
      f'to X = {character_arr[chosen_character_index].GetX()} '
      f'and Y = {character_arr[chosen_character_index].GetY()}')


# -----------------------------------------------------------------------------------
Queue = [0 for _ in range(100)]
test_queue = [0, 0, 0]
headPointer = 0
tailPointer = -1


def Enqueue(item):
    global Queue, tailPointer
    success = False
    if tailPointer == len(Queue) - 1:
        tailPointer = 0
        Queue[tailPointer] = item
        success = True
    else:
        tailPointer += 1
        Queue[tailPointer] = item
        success = True
    return str(success).upper()


for i in range(1, 21):
    successful = Enqueue(i)
    if not successful:
        print('Unsuccessful')
        break
    else:
        print('Successful')


print(Queue)
print(tailPointer)  # --> 19


# - Write the normal one and amend the program to recursive function
# - and check whether the result is the same.
# NOT RECURSIVE EDITION
def IterativeOutput(start: int):
    total = 0
    for counter in range(start, headPointer - 1, - 1):
        total += Queue[counter]
    return total


print(f'The non-recursive output is: {IterativeOutput(19)}')


# RECURSIVE EDITION
def Recur_IterativeOutput(start: int):
    if start == headPointer:
        return Queue[start]
    else:
        return Queue[start] + Recur_IterativeOutput(start - 1)


print(f'The recursive output is: {Recur_IterativeOutput(19)}')
