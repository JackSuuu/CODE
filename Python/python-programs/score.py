

list = [ ]
counts = 1
while counts <= 10:
    
    score = input("please enter you score ")
    score = int(score)

    if score <= 100 and score >= 0:
       list.append(score)
       counts += 1
    else:
        print("your score is invalid, please enter the score in range 0 to 100")
        break

Flist = len(list)

if Flist == 10:
    B = sum(list)
    C = len(list)
    A = B/C
    print("\n")
    print('the average score is',A)
    print('the score list is')
    print(list)
else:
    print("the list haven't completed yet,please restart the program again")
    




   


      


    
