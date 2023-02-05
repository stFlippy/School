from random import randint


class Human:
    def __init__(self, name):
        self.action = None
        self.house = None
        self.fullness = 50
        self.name = name
        self.dead = False

    def __str__(self):
        return 'Теущая сытость {} = {}'.format(self.name, self.fullness)

    def move_to_house(self, name):
        self.house = name
        self.fullness -= 10
        return '{} заселился в {}'.format(self.name, self.house)

    def eat(self):
        if self.house.food < 10:
            self.get_food()
            return 'Eсть нечего, пошел в магаз'

        else:
            self.house.food -= 10
            self.fullness += 20
            return 'Чел перекусил'

    def get_food(self):
        self.fullness -= 5
        if self.house.money < 50:
            self.go_to_work()
            return 'Денюх нет, пошёл работать ;('
        elif self.house.money >= 100:
            self.house.money -= 100
            self.house.cat_food += 50
            self.house.food += 50
            return 'Ну терь пожрем'
        if self.house.money < 100:
            self.house.food += 50
            self.house.money -= 50
            return 'А Като печенек не заслужил)'

    def get_cat_food(self):
        self.fullness -= 5
        if self.house.money < 50:
            self.go_to_work()
            return 'Денюх нет, пошёл работать ;('
        elif self.house.money >= 100:
            self.house.money -= 100
            self.house.cat_food += 50
            self.house.food += 50
            return 'Ну терь пожрем'
        if self.house.money < 100:
            self.house.cat_food += 50
            self.house.money -= 50
            return 'Жри котяра ебаная'

    def go_to_work(self):
        self.fullness -= 20
        self.house.money += 150
        self.eat()
        return 'Стописят на бочку))'

    def act(self):
        if self.fullness <= 0:
            self.dead = True
            return '{} помер в триумфальных голодных конвульсиях'.format(self.name)
        if self.fullness <= 10:
            return self.eat()
        if self.house.purity <= 10:
            return self.clearing()

        self.action = randint (1,8)

        if 1 <= self.action <= 2:
            return self.get_food()
        elif 3 <= self.action <= 4:
            return self.clearing()
        elif 5 <= self.action <= 7:
            return self.chill()
        elif self.action == 8:
            return self.go_to_work()
        else:
            return 'Все пошло по звезде'

    def clearing(self):
        self.house.purity += 50
        self.fullness -= 10
        return 'Прибрался малях'

    def chill(self):
        self.fullness -= 10
        return 'Прокрастинация'


class Cato:
    def __init__(self, name):
        self.house = None
        self.fullness = 20
        self.name = name
        self.action = 0

    def __str__(self):
        return 'Текущая сытость {} ='.format(self.name), self.fullness

    def move_to_house(self, house):
        self.house = house

    def sleep(self):
        self.fullness -= 10
        return 'Кот Проспал весь день, ска'

    def eat(self):
        if self.house.cat_food >= 10:
            self.house.cat_food -= 10
            self.fullness += 20
            return 'Кот весь день жрал, когда ж ты лопнешь? о_О'
        else:
            print('{} кушац нечего(('.format(self.name))

    def litter(self):
        self.house.purity -= 5
        self.fullness -= 10
        return 'Эта кошка ещё и стены все ободрала, нахрен я его держу?'

    def act(self):
        if self.fullness <= 0:
            del self
            return 'Като помер как герой'
        elif self.fullness <= 10:
            return self.eat()
        else:
            self.action = randint(1, 3)
            if self.action == 1:
                if self.house.cat_food >= 10:
                    return self.eat()
            elif self.action == 2:
                return self.litter()
            elif self.action == 3:
                return self.sleep()
            else:
                return 'Като шредингера'


class House:
    def __init__(self):
        self.purity = 100
        self.food = 50
        self.money = 50
        self.cat_food = 0

    def __str__(self):
        return 'Остаток еды = {}, остаток денег = {}, чистота = {}, кошачья еда = {}'.format(self.food, self.money, self.purity, self.cat_food)
