

# (a)
player_names_arr = ['None' for _ in range(11)]
player_score_arr = [-1 for _ in range(11)]
# arr = [['none'] * 2 for _ in range(5)]
# arr[0][0] = 'A'
# print(arr)


def ReadHighScores():
    try:
        with open('HighScore.txt', 'r') as File:
            player_name = str(File.readline().strip())
            count = 0
            while player_name != '':
                player_score = int(File.readline().strip())
                player_names_arr[count] = player_name
                player_score_arr[count] = player_score
                count += 1
                player_name = str(File.readline().strip())
    except IOError:
        print("File not find")


def OutPutHighScores():
    for i in range(len(player_names_arr)):
        print(f'{player_names_arr[i]} {player_score_arr[i]}')


ReadHighScores()
# OutPutHighScores()
print(player_names_arr, player_score_arr)


newPlayerName = 'GGG'
newPlayerScore = 9999
while newPlayerScore < 1 or newPlayerScore > 100000:
    newPlayerName = input("Enter the player name")
    newPlayerScore = input("Enter the player score")

    print("The score should be in between 1-100000")


# TODO: SORT IN ORDER -->
# 确认是否有重复的数字
def CreateNewTopTen(playerName: str, playerScore: int):
    global player_names_arr, player_score_arr
    if newPlayerScore is not None:
        player_score_arr[-1] = playerScore
        player_score_arr.sort(reverse=True)
        insert_index = player_score_arr.index(playerScore)
        player_names_arr.insert(insert_index, playerName)
    else:
        return "The Player Score is not fit requirement"



print(player_names_arr, player_score_arr)
CreateNewTopTen(newPlayerName, newPlayerScore)
print(player_names_arr, player_score_arr)


def WriteTopTen():
    with open('NewHighScore.txt', 'w') as NewFile:
        for i in range(len(player_names_arr) - 2):
            new_player_name = str(player_names_arr[i])
            new_player_score = str(player_score_arr[i])
            NewFile.writelines(new_player_name + '\n')
            NewFile.writelines(new_player_score + '\n')


WriteTopTen()


x = '''
s
s
s
'''

y = "" \
    "" \
    ""
