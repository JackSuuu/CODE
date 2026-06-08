
# CIE_真题/9618_s21_qp_41.pdf
# Question 3

class TreasureChest:
    # Private question: String
    # Private answer: Integer
    # Private points: Integer
    def __init__(self, question: str, answer: int, points: int):
        self.__question = question
        self.__answer = answer
        self.__points = points

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, user_answer):
        if user_answer == self.__answer:
            return True
        else:
            return False

    def getPoints(self, attempt):
        if attempt == 1:
            return self.__points
        elif attempt == 2:
            return int(self.__points / 2)
        elif attempt == 3 or 4:
            return int(self.__points / 4)
        else:
            return 0


def readData():
    arrayTreasure = []
    try:
        with open("../CIE_真题/File/TreasureChestData.txt", 'r') as file:
            count = 0
            question = ''
            str_line = file.readline().strip()  # using strip to get rid of \n
            while str_line != "":
                if count == 0:
                    question = str_line
                    count += 2
                elif count == 1:
                    str_line = file.readline().strip()
                    question = str_line
                    count += 1
                elif count == 2:
                    str_line = file.readline().strip()
                    answer = int(str_line)
                    count += 1
                if count == 3:
                    str_line = file.readline().strip()
                    points = int(str_line)
                    treasureData = TreasureChest(question, answer, points)
                    arrayTreasure.append(treasureData)
                    count = 1
            return arrayTreasure
    except IOError:
        print("file not in the directory")


Data = readData()
questionNumber = int(input("Please enter a question number between 1-5:")) - 1
print(Data[questionNumber].getQuestion())

is_correct = Data[questionNumber].checkAnswer(int(input("Please enter your answer:")))
user_attempt = 1
awarded_point = 0

while not is_correct:
    print(f"Your answer is {is_correct}, please try it again")
    print(Data[questionNumber].getQuestion())
    is_correct = Data[questionNumber].checkAnswer(int(input("Please enter your answer:")))
    user_attempt += 1

awarded_point += Data[questionNumber].getPoints(user_attempt)
print("Your are correct, your awarded point is: " + str(awarded_point))
