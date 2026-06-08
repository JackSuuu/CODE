
final_mark = 0

def isCorrect(x):
    return x == 10

def countMark(mark):
    global final_mark
    final_mark + 1 if isCorrect(mark) else final_mark

def _countMark_(mark, final:int):
    if isCorrect(mark):
        return (final + 1)

final_mark = _countMark_(10, final_mark)
final_mark = _countMark_(9, final_mark)
final_mark = _countMark_(10, final_mark)

print(final_mark)

