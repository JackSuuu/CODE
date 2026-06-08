

# 9618_w22_42-Q2
class Character:
    def __init__(self, Name: str, XCoordinate: int, YCoordinate: int):
        self.__Name = Name
        self.__XCoordinate = XCoordinate
        self.__YCoordinate = YCoordinate

    def GetName(self):
        return self.__Name

    def GetX(self):
        return self.__XCoordinate

    def GetY(self):
        return self.__YCoordinate

    def ChangePosition(self, Xchange, Ychange):
        self.__XCoordinate += Xchange
        self.__YCoordinate += Ychange


character_arr = [Character('', 0, 0) for _ in range(10)]

with open("../CIE_真题/File/9618_w22_sf_42/"
          "11_9618_42_Confidential Source Files November 2022/"
          "Characters.txt", "r") as character_file:
    char_name = character_file.readline().strip().lower()
    count = 0
    while char_name != '':
        x_cor = int(character_file.readline().strip())
        y_cor = int(character_file.readline().strip())
        character_arr[count] = Character(char_name, x_cor, y_cor)
        char_name = str(character_file.readline().strip()).lower()
        count += 1


print(character_arr[2].GetName())

success_search = False
index = 0
while not success_search:
    # TODO: edit back to input
    search_char = input("Enter the character name: ").lower()
    for i in range(10):
        if search_char == character_arr[i].GetName():
            index = i
            success_search = True


print(index)
valid_move = False
char_dict = {'A': - 1, 'W': + 1, 'S': - 1, 'D': + 1}
direction_dict = {'A': 'X', 'W': 'Y', 'S': 'Y', 'D': 'X'}
print(char_dict.keys())
input_char = ''
change_corr = ''
while not valid_move:
    input_char = input("Enter the valid character move: ")
    if input_char in char_dict.keys():
        change_corr = direction_dict[input_char]  # X or Y
        change_val = char_dict[input_char]  # -1 or +1
        if change_corr == 'X':
            character_arr[index].ChangePosition(change_val, 0)
        else:
            character_arr[index].ChangePosition(0, change_val)
        print(f"{character_arr[index].GetName()} "
              f"has changed coordinates to X = {character_arr[index].GetX()}"
              f" and Y = {character_arr[index].GetY()}")
        valid_move = True

# ENTER: THOMAS, qui, X, A
