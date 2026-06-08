def fizzBuzz(n):
    word = ""
    # Write your code here
    for i in range(n):
        if (i % 3 == 0):
            word += "Fizz"
        if (i % 5 == 0):
            word += "Buzz"
        if (word != ""): 
            print(word)
            word = ""
        else:
            print(i)

fizzBuzz(15)