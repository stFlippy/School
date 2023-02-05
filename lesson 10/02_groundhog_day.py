# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.


ENLIGHTENMENT_CARMA_LEVEL = 777

# TODO здесь ваш код

from random import randint
from libs.exc_10_2 import IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError
karma = 0

with open('log.txt', mode='w'):
    pass

while 1:
    if karma >= ENLIGHTENMENT_CARMA_LEVEL:
        break

    try:
        today = randint(1, 13)

        if today == 1:
            raise IamGodError()

        elif today == 2:
            raise DrunkError

        elif today == 3:
            raise CarCrashError

        elif today == 4:
            raise GluttonyError

        elif today == 5:
            raise DepressionError

        elif today == 6:
            raise SuicideError

        else:
            karma += today

    except Exception as nme:

        # print(f'ошибка - {nme}')
        with open('log.txt', mode='a') as log:
            log.writelines(str(nme) + '\n')

print(f'мы выбрались из этого дерьма амиго, твоя карма = {karma}')


# https://goo.gl/JnsDqu
