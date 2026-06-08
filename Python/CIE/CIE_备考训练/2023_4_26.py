
class Card:
    def __init__(self, Number: int, Colour: str):
        self.__Number = Number  # PRIVATE INTEGER
        self.__Colour = Colour  # PRIVATE STRING

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


Card_arr = [Card(0, '') for _ in range(30)]
try:
    with open('txt-文件/CardValues.txt', 'r') as FILE:
        number = FILE.readline().strip()
        count = 0
        while number != '':
            colour = FILE.readline().strip()
            Card_arr[count] = Card(int(number), str(colour))
            number = FILE.readline().strip()
            count += 1
except IOError:
    print("Error occur while input file")


# allow all players to select 4 cards from the 30.
# A card can only be selected once,
# so the program needs to record which cards have already been used
used_arr = []


def ChooseCard():
    global used_arr
    index = int(input("Enter an index between 1-30: "))
    while (index - 1) < 0 or (index - 1) > 29:
        index = int(input("Not in range, Enter again: "))
    while (index - 1) in used_arr:
        index = int(input("Already selected, Enter again: "))
    print(used_arr)
    return index


Player1 = [Card(0, '')]  # TYPE: CARDS
# used_arr.append(ChooseCard() - 1)
# used_arr.append(ChooseCard() - 1)
# used_arr.append(ChooseCard() - 1)
# used_arr.append(ChooseCard() - 1)
# for each in used_arr:
#     Player1.append(Card_arr[each])
# for i in range(len(Player1)):
#     if i != 0:
#         print("The card number is", Player1[i].GetNumber())
#         print("The card colour is", Player1[i].GetColour())


# -------------------------------------------------------------------------------
class Card:
    def __init__(self, Number: int, Colour: str):
        self.__Number = Number  # PRIVATE INTEGER: 1-5
        self.__Colour = Colour  # PRIVATE STRING: red, blue or yellow

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


card_1 = Card(1, 'red')
card_2 = Card(2, 'red')
card_3 = Card(3, 'red')
card_4 = Card(4, 'red')
card_5 = Card(5, 'red')
card_6 = Card(1, 'blue')
card_7 = Card(2, 'blue')
card_8 = Card(3, 'blue')
card_9 = Card(4, 'blue')
card_10 = Card(5, 'blue')
card_11 = Card(1, 'yellow')
card_12 = Card(2, 'yellow')
card_13 = Card(3, 'yellow')
card_14 = Card(4, 'yellow')
card_15 = Card(5, 'yellow')


class Hand:
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__Cards = [Card(0, '') for _ in range(10)]  # PRIVATE ARRAY[0:9]
        self.__Cards[0] = Card1  # PRIVATE CARD
        self.__Cards[1] = Card2  # PRIVATE CARD
        self.__Cards[2] = Card3  # PRIVATE CARD
        self.__Cards[3] = Card4  # PRIVATE CARD
        self.__Cards[4] = Card5  # PRIVATE CARD
        self.__FirstCard = 0  # PRIVATE INTEGER
        self.__NumberCard = 5  # PRIVATE INTEGER

    def GetCard(self, index):
        return self.__Cards[index]


PPlayer1 = Hand(card_1, card_2, card_3, card_4, card_11)
PPlayer2 = Hand(card_12, card_13, card_14, card_15, card_6)


def CalculateValue(Player_Hand: Hand):
    player_score = 0
    for n in range(5):
        score = Player_Hand.GetCard(n)
        if score.GetColour() == 'red':
            player_score += 5
        elif score.GetColour() == 'blue':
            player_score += 10
        elif score.GetColour() == 'yellow':
            player_score += 15
        player_score += score.GetNumber()
    return player_score


PPlayer1_Score = CalculateValue(PPlayer1)
PPlayer2_Score = CalculateValue(PPlayer2)

if PPlayer1_Score >= PPlayer2_Score:
    if PPlayer1_Score == PPlayer2_Score:
        print("Draw")
    else:
        print("Player 1 is winner")
else:
    print("Player 2 is winner")


# -------------------------------------------------------------------------------
class Node:
    def __init__(self, data: int, nextNode: int):
        self.data = data  # INTEGER
        self.nextNode = nextNode  # INTEGER


linkedList = [Node(1, 1), Node(5, 4), Node(6, 7), Node(7, -1),
              Node(2, 2), Node(0, 6), Node(0, 8), Node(56, 3),
              Node(0, 9), Node(0, -1)]
startPointer = 0
emptyList = 5


def outputNodes(start_pointer):
    curr_pointer = start_pointer
    while curr_pointer != -1:
        print(linkedList[curr_pointer].data)
        curr_pointer = linkedList[curr_pointer].nextNode


def addNode(LinkedList, start_pointer: int):
    global emptyList
    item = int(input("Enter the new data: "))
    if emptyList != -1:
        LinkedList[emptyList].data = item
        curr_pointer = start_pointer
        while LinkedList[curr_pointer].nextNode != -1:
            curr_pointer = LinkedList[curr_pointer].nextNode
        last_pointer = curr_pointer
        tem_pointer = emptyList
        LinkedList[last_pointer].nextNode = emptyList
        emptyList = LinkedList[emptyList].nextNode
        LinkedList[tem_pointer].nextNode = -1
        return True
    else:
        return False


print("# ---QUESTION (d)(i) SECTION---")
outputNodes(startPointer)
Add = addNode(linkedList, startPointer)
if Add:
    print("Add successfully")
else:
    print("Not add")
outputNodes(startPointer)

# test value: 5
