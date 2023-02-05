# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42
input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
leeloo = 0
try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result:*^30}!")

except IndexError as err:
    print(f'{err}  |  {err.args}')

except ValueError as err:
    print(f'{leeloo}  |  {err.args}')

except:
    print(f'шото ваще пздц')

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения\
# для каждого типа исключений написать на консоль соотв. сообщение




