

# print(13//2)
print("===================== QUESTION ONE ============================")


def Unknown(X: int, Y: int):
    if X < Y:
        print(X + Y)
        return Unknown(X + 1, Y) * 2
    else:
        if X == Y:
            return 1
        else:
            print(X + Y)
            return Unknown(X - 1, Y) // 2


X1 = 10
Y1 = 15
X2 = 10
Y2 = 10
X3 = 15
Y3 = 10

print(f"Parameters: X={X1}, Y={Y1}")
print("Return value", Unknown(X1, Y1))
print("=================================================")
print(f"Parameters: X={X2}, Y={Y2}")
print("Return value", Unknown(X2, Y2))
print("=================================================")
print(f"Parameters: X={X3}, Y={Y3}")
print("Return value", Unknown(X3, Y3))
print("=================================================")


def IterativeUnknown(X, Y):
    RETURN_VALUE = 1
    COUNT = 0
    if X < Y:
        OP = 'X BIGGER'
    else:
        OP = 'Y BIGGER'
    while X != Y:
        if X < Y:
            print(X + Y)
            X += 1
        else:
            if X == Y:
                break
            else:
                print(X + Y)
                X -= 1
        COUNT += 1

    for i in range(COUNT):
        if OP == 'X BIGGER':
            RETURN_VALUE *= 2
        else:
            RETURN_VALUE //= 2
    return RETURN_VALUE


print("Return value", IterativeUnknown(10, 15))
print("===================== QUESTION TWO ============================")


class Picture:
    def __init__(self, Description: str, Width: int, Height: int, FrameColour: str):
        self.__Description = Description  # PRIVATE STRING
        self.__Width = Width  # PRIVATE INTEGER
        self.__Height = Height  # PRIVATE INTEGER
        self.__FrameColour = FrameColour  # PRIVATE STRING

    def GetDescription(self):
        return self.__Description

    def GetHeight(self):
        return self.__Height

    def GetWidth(self):
        return self.__Width

    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self, NewDescription):
        self.__Description = NewDescription


Pic_arr = [Picture('', 0, 0, '') for _ in range(100)]


def ReadData():
    try:
        with open("txt-文件/Pictures.txt", 'r') as FILE:
            count = 0
            desc = str(FILE.readline().strip())
            while desc != '':
                wid = int(FILE.readline().strip())
                hei = int(FILE.readline().strip())
                col = str(FILE.readline().strip())
                Pic_arr[count] = Picture(desc, wid, hei, col)
                desc = str(FILE.readline().strip())
                count += 1
    except IOError:
        print("THE FILE IS NOT OPEN CORRECTLY!")
    return "The number of pictures are" + str(count)


ReadData()
# MAIN PROGRAM SECTION
ColourOfTheFrame = 'silver'  # str(input("Please enter the colour: ")).lower()
MaximumWidth = 25  # int(input("Please enter maximum colour: "))
MaximumHeight = 25  # int(input("Please enter maximum height: "))
for EachPicture in Pic_arr:
    if EachPicture.GetColour() == ColourOfTheFrame:
        if EachPicture.GetWidth() >= MaximumWidth and EachPicture.GetHeight() >= MaximumHeight:
            print(EachPicture.GetDescription())

print("===================== QUESTION THREE ============================")

# Declare Binary trees and its nodes
ArrayNodes = [[0 for X in range(3)] for Y in range(20)]
print(ArrayNodes)
RootPointer = -1
FreeNode = 0


def AddNode(NodeData):
    global ArrayNodes, RootPointer, FreeNode
    # NodeData = int(input("Enter the data: "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed is False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode += 1
    else:
        print("Tree is full")


def PrintAll():
    global ArrayNodes
    for Nodes in ArrayNodes:
        LeftP = Nodes[0]
        Data = Nodes[1]
        RightP = Nodes[2]
        print(f"LeftPointer: {LeftP} | Data: {Data} | RightPointer: {RightP}")


Data_arr = [10, 5, 15, 8, 12, 6, 20, 11, 9, 4]
for Data in Data_arr:
    AddNode(Data)
PrintAll()


def InOrder(Tree, CurrNode):
    if Tree[CurrNode][0] != -1:
        InOrder(Tree, Tree[CurrNode][0])
    print(str(Tree[CurrNode][1]))
    if Tree[CurrNode][2] != -1:
        InOrder(Tree, Tree[CurrNode][2])


InOrder(ArrayNodes, RootPointer)
