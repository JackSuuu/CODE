
class Picture:
    # Private description: STRING
    # Private width: INTEGER
    # Private height: INTEGER
    # Private frame_colour: STRING
    def __init__(self, description: str, width: int, height: int, frame_colour: str):
        self.__description = description  # string
        self.__width = width  # integer
        self.__height = height  # integer
        self.__frame_colour = frame_colour  # string

    def getDescription(self):
        return self.__description

    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width

    def getColour(self):
        return self.__frame_colour

    def setDescription(self, new_description):
        self.__description = new_description


picture_array = []
for i in range(100):
    picture_array.append(Picture('', 0, 0, ''))


def readData():
    try:
        with open("../CIE_真题/File/Pictures.txt", 'r') as picture_file:
            count_number = 0
            file_description = picture_file.readline().strip()
            while file_description != '':
                file_width = picture_file.readline().strip()
                file_height = picture_file.readline().strip()
                file_colour = picture_file.readline().strip().lower()
                picture_array[count_number] = Picture(file_description, int(file_width), int(file_height), file_colour)
                file_description = picture_file.readline().strip()
                count_number += 1
    except IOError:
        print("file not in the directory")
    finally:
        print("ERROR")
    return count_number  # , picture_array


print("The number of picture is", readData())

# Main program to accept the user input
# 最好将 input 拆分开来写！！
user_requirement = input("Please enter your requirement(colour,maximum width,maximum height): ")
print('---------------------')
requirement_arr = user_requirement.split(',')
user_colour_choice = requirement_arr[0].lower()
user_maximum_width = int(requirement_arr[1])
user_maximum_height = int(requirement_arr[2])

for i in range(len(picture_array)):
    if picture_array[i].getDescription() != '':
        if picture_array[i].getColour() == user_colour_choice:
            if picture_array[i].getWidth() <= user_maximum_width and \
                    picture_array[i].getHeight() <= user_maximum_height:
                print(f"The picture '{picture_array[i].getDescription()}' is fit your requirement")
                print(f"The picture's Width is {picture_array[i].getWidth()}")
                print(f"The picture's Height is {picture_array[i].getHeight()}")
                print("---------------------")
    else:
        break
