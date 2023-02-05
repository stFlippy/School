
class Human:

    def __init__(self, name):
        self.name = name
        self.house = None
        self.fullness = 30
        self.happyness = 100

    def __str__(self):
        return '{} появился'.format(self.name)


class House:

    def __init__(self):
        self.cash = 150
        self.food = 50
        self.purity = 0
