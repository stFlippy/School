# -*- coding: utf-8 -*-

import zipfile
from typing import Tuple


from pprint import pprint


# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  |  9999999 |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код


class StatCharFile:

    def __init__(self, file_name):
        self.file_name = file_name
        self.name_list = None
        self.dict_array = {}
        self.sorted_dic = {}
        self.book = {}

    def __str__(self):
        return self.dict_array

    def extract_file(self):
        z_file = zipfile.ZipFile(self.file_name)
        self.name_list = z_file.namelist()
        if self.name_list:
            for name in self.name_list:
                z_file.extract(name)
            return f'Извлечены следующие файлы:\n{self.name_list}'
        else:
            return 'Архив пуст'

    def collect_data(self):
        # if self.name_list:
        with open(self.name_list[0], 'r') as src:
            for string in src:
                for char in string:
                    if char.isalpha():
                        if char.lower() in self.dict_array:
                            self.dict_array[char.lower()] += 1
                        else:
                            self.dict_array[char.lower()] = 1

    def my_pprint(self):
        print(f'+----------+-----------+', end='\n')
        print(f'|--Символ--+Количество-|', end='\n')
        print(f'+----------+-----------+', end='\n')
        for subj in self.dict_array:
            print(f'|{subj:^10}|{self.dict_array[subj]:^11}|')
            # print(self.dict_array[subj])
            pass
        # print(f'+----------+-----------+', end='\n')
        # print(self.dict_array)

    def sort(self, method):
        if method == 'ascending_alpha':
            sorted_dic = {}
            ref_mask = sorted(self.dict_array.keys())
            for itm in ref_mask:
                for key in self.dict_array:
                    if key == itm:
                        sorted_dic[key] = self.dict_array[key]
                        self.dict_array.pop(key)
                        break
            self.dict_array = {}
            self.dict_array = sorted_dic
            return None

        elif method == 'discending_alpha':
            sorted_dic = {}
            ref_mask = sorted(self.dict_array.keys(), reverse=True)
            for itm in ref_mask:
                for key in self.dict_array:
                    if key == itm:
                        sorted_dic[key] = self.dict_array[key]
                        self.dict_array.pop(key)
                        break
            self.dict_array = {}
            self.dict_array = sorted_dic
            return None

        elif method == 'ascending_count':
            sorted_dic = {}
            ref_mask = sorted(self.dict_array.values())
            for itm in ref_mask:
                for key in self.dict_array:
                    if self.dict_array[key] == itm:
                        sorted_dic[key] = self.dict_array[key]
                        self.dict_array.pop(key)
                        break
            self.dict_array = {}
            self.dict_array = sorted_dic
            return None

        elif method == 'discending_count':
            sorted_dic = {}
            ref_mask = sorted(self.dict_array.values(), reverse=True)
            for itm in ref_mask:
                for key in self.dict_array:
                    if self.dict_array[key] == itm:
                        sorted_dic[key] = self.dict_array[key]
                        self.dict_array.pop(key)
                        break
            self.dict_array = sorted_dic
            return None


file = StatCharFile('.//python_snippets//voyna-i-mir.txt.zip')

print(file.extract_file())

file.collect_data()

file.sort('ascending_count')

file.my_pprint()

# print(file.dict_array)



# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
