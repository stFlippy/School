#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
mfm = my_favorite_movies

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# TODO здесь ваш код

print   (mfm[:mfm.index(',')])
new_mfm = mfm[::-1]
print   (mfm[len(mfm)-new_mfm.index(',') + 1:])
print   (mfm.count)
