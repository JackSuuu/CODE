# PyType is a python implemented terminal typing app
# Which you can run directly in terminal and 
# gives you the smooth experience of testing your typing speed

from random_word import RandomWords

rw = RandomWords()
# get the random words from the rw
random_word = rw.get_random_word()

word_list = [rw.get_random_word]

word_to_type = "Hello"

for each in word_to_type:
    print(each)
    type_word = input()
    if type_word == each:
        print("CORRECT")

