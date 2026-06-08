
try:
    file = open("CIE_真题/File/TreasureChestData.txt", "r")
    count = 1
    str_line = file.readline().strip()
    while str_line != "":
        if count == 1:
            print("question")
            count += 1
        elif count == 2:
            print("answer")
            count += 1
        elif count == 3:
            print("point")
            count = 1
        print(str_line)
        str_line = file.readline().strip()
except IOError:
    print("file not found")