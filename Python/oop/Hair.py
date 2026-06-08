
class Hair:
    def __init__(self, color='black'):
        self.color = color

    def great_hair_style(self):
        if self.color == 'black':
            print('black is the best hair color')
        else:
            print('your color is suck')


Janet = Hair('blue')
print(Janet.color)
Janet.great_hair_style()