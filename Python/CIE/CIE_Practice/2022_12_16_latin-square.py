
# Definition of Latin Square
# row can column can not repeat
# each row and column contains the same number
# solution: compare row and column sum and number

false1 = "Latin-square/false1.txt"
false2 = "Latin-square/false2.txt"
true1 = "Latin-square/true.txt"
true2 = "Latin-square/true2.txt"


def latinSquare(file):
    list_2d = []
    # Read file into 2d array
    with open(file, 'r') as fp:
        line = fp.readline()
        while line != "":
            line = line.strip("\n")
            tem_list = line.split(",")
            list_2d.append(tem_list)
            line = fp.readline()

        col_list = []
        length_2d = len(list_2d)

        for i in range(length_2d):
            for j in range(length_2d):
                row_sum = 0
                col_sum = 0
                for k in range(length_2d):
                    row_sum += int(list_2d[j][k])
                    col_sum += int(list_2d[k][j])
                    col_list.append(list_2d[k][j])
                # check row_sum and col_sum, get intersection compare to length_2d
                row_list = list_2d[i]
                if row_sum != col_sum:
                    return False
                elif len(set(row_list) & set(col_list)) != length_2d:
                    return False
                col_list.clear()

        return list_2d, True


print(latinSquare(true2))
