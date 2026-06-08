

class HiddenWord:
    def __init__(self, hidden_word: str):
        self.hidden_word = hidden_word

    def getHint(self, guess_word: str):
        # You may assume that the length of the guess is the same as the length of the hidden word.
        words = ''
        for i in range(len(self.hidden_word)):
            flag = False
            if guess_word[i] != self.hidden_word[i]:
                for word in self.hidden_word:
                    if guess_word[i] == word:
                        flag = True
                if flag is True:
                    words += '+'
                else:
                    words += '*'
            else:
                words += self.hidden_word[i]
        return words


puzzle = HiddenWord("HARPS")
print(puzzle.getHint("AAAAA"))
print(puzzle.getHint("HELLO"))
print(puzzle.getHint("HEART"))
print(puzzle.getHint("HARMS"))
print(puzzle.getHint("HARPS"))
