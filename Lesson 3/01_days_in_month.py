# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом

# TODO здесь ваш код
while 1:
    user_input = input("Введите, пожалуйста, номер месяца: ")
    month = int(user_input)
    print('Вы ввели', month)
    if 1 <= month <= 12:
        if 1 <= month <= 7:
            if month % 2 == 0:
                if month == 2:
                    print('28')
                else:
                    print('30')
            else:
                print('31')
        if 8 <= month <= 12:
            if month % 2 == 0:
                print('31')
            else:
                print('30')
        print(' дней/день')
    else:
        print("sasat')")
