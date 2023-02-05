class NameIsNotCorrect(Exception):
    def __str__(self):
        return 'Не верное имя пользователя'


class AgeIsNotCorrect(Exception):
    def __str__(self):
        return 'Возраст указан не верно'


class MailIsNotCorrect(Exception):
    def __str__(self):
        return 'Не верный адрес электронной почты'


class NotEnoughData(Exception):
    def __str__(self):
        return 'Указаны не все данные'


def init():
    with open('registrations_good.log', mode='w'):
        pass

    with open('registrations_bad.log', mode='w'):
        pass

def write_good(line):
    with open('registrations_good.log', mode='a', encoding='utf-8') as ostream:
        ostream.writelines(line)

def write_bad(line):
    with open('registrations_bad.log', mode='a', encoding='utf-8') as ostream:
        ostream.writelines(line)

