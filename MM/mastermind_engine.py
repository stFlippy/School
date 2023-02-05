from random import randint
from pprint import pprint

_src_num = 0
_win = False
_dic_of_digits = {}


def init():
    global _src_num
    global _dic_of_digits
    global _win
    print("Приветствую вас в игре БЫКИ и КОРОВЫ")
    print("И так, я задумал число от 1000 до 9999, постарайтесь отгадать его.... ;)")
    print("Введите help, что бы ознакомиться с правилами игры\n")
    _win = False
    _src_num = randint(1000, 9999)
    for char in str(_src_num):
        if _dic_of_digits.__contains__(char):
            _dic_of_digits[char] += 1
        else:
            _dic_of_digits[char] = 1


def check_num(usr_num):
    bulls = 0
    cows = 0
    temp_dic = _dic_of_digits.copy()
    for i, char in enumerate(usr_num):
        if char == str(_src_num)[i]:
            bulls += 1
        if temp_dic.__contains__(char):
            if temp_dic[char] > 0:
                cows += 1
                temp_dic[char] -= 1
    if bulls == 4:
        global _win
        _win = True
    return {'cows': cows - bulls, 'bulls': bulls}


def game_over():
    if _win:
        print("Победа")
        return True


def help_me():
    pprint("""Быки и коровы — логическая игра, в ходе которой за несколько попыток один из игроков должен 
           определить, что задумал другой игрок.В классическом варианте игра рассчитана на двух игроков. 
           Каждый из игроков задумывает и записывает тайное 4-значное число с неповторяющимися цифрами. 
           Игрок, который начинает игру по жребию, делает первую попытку отгадать число. 
           Попытка — это 4-значное число с неповторяющимися цифрами, сообщаемое противнику. 
           Противник сообщает в ответ, сколько цифр угадано без совпадения с их позициями в тайном числе 
           (то есть количество коров) и сколько угадано вплоть до позиции в тайном числе (то есть количество быков).
           Например: 
           Задумано тайное число «3219». 
           Попытка: «2310».
           Результат: две «коровы» (две цифры: «2» и «3» — угаданы на неверных позициях) и один «бык» 
           (одна цифра «1» угадана вплоть до позиции).""")
    print("И так, я задумал число от 1000 до 9999, постарайтесь отгадать его.... ;)\n")


def im_cheater():
    print(_src_num)


def input_num(num):
    global _src_num
    _src_num = num
