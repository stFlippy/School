# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

# TODO здесь ваш код

from libs.exc_10_3 import init, AgeIsNotCorrect, NameIsNotCorrect, MailIsNotCorrect, NotEnoughData, write_good, \
    write_bad


def body():
    init()
    with open('registrations.txt', mode='r', encoding='utf-8') as src:
        for line in src:
            if not len(line) <= 1:

                try:

                    print(line)
                    array = line.split(' ')

                    if not len(array) == 3:
                        raise NotEnoughData

                    if not array[0].isalpha():
                        raise NameIsNotCorrect

                    if array[1].find('.') < 1 or array[1].find('@') < 2:
                        raise MailIsNotCorrect

                    array[2] = array[2][:-1]

                    if not 10 < int(array[2]) < 100:
                        raise AgeIsNotCorrect

                    write_good(line)

                except Exception as excptn:
                    print(f'Словили ошибку — {excptn}')
                    write_bad(f'{line[:-1]} — {excptn}\n')

body()
