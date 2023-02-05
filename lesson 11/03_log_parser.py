# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

# TODO здесь ваш код

import lib_for_ev_parser as lib


def ev_iterrator(input_data):
    data_list = []
    for string in input_data:
        data_list.append(string[1:-1])
    data_list = list(filter(lambda x: x[28:31] == 'NOK', data_list))
    str_num = 0

    while str_num <= len(data_list):
        curr_time = data_list[str_num][0:16]
        event_counter = 1
        str_num += 1
        if str_num == len(data_list):
            yield curr_time, event_counter
            return

        while curr_time == data_list[str_num][0:16]:
            event_counter += 1
            str_num += 1
            if str_num == len(data_list):
                return

        yield curr_time, event_counter


with open('events.txt', mode='r') as inpt:
    grouped_events = lib.EventIterrator(inpt)

with open('events.txt', mode='r') as inpt:
    for time, counter in ev_iterrator(inpt):
        print(f'[{time}] {counter}')

# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
