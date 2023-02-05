# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# smpls = get_prime_numbers(5)
# print(smpls)

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.smpl_nums = [2]
        self.num = 1
        self.end = n

    def __iter__(self):
        # self.num = 1
        return self

    def __next__(self):
        while len(self.smpl_nums) <= self.end:
            self.num += 1
            for i in self.smpl_nums:
                if self.num % i == 0:
                    break
                if i == self.smpl_nums[-1]:
                    self.smpl_nums.append(self.num)
                    return self.smpl_nums[-2]
        raise StopIteration

    # TODO здесь ваш код


# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)
#     break


# TODO после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    simpl_nums = [2]
    yield 2
    for i in range(2, n + 1):
        for num in simpl_nums:
            if i % num == 0:
                break
            if num > i // 2:
                simpl_nums.append(i)
                yield i
                break

    # TODO здесь ваш код


# for number in prime_numbers_generator(n=100000):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def is_lucky_num(x):
    front, back = 0, 0
    num_length = len(str(x))
    for pos in range(0, num_length // 2):
        front += int(str(x)[pos])
        back += int(str(x)[-pos - 1])
    return front == back


def is_polyndrome(x):
    num_length = len(str(x))
    for pos in range(0, num_length // 2):
        front = int(str(x)[pos])
        back = int(str(x)[-pos - 1])
        if front != back:
            return False
    return True


lst = [54545, 436789, 101, 92083, 727]
lucky_lst = filter(is_lucky_num, lst)
print(list(lucky_lst))

lucky_lst = filter(is_polyndrome, PrimeNumbers(20))
print(list(lucky_lst))
