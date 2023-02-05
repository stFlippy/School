# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'

def log_errors(log_name):
    def function(func):
        def executer(arg):
            try:
                return func(arg)

            except Exception as info:
                with open(log_name, mode='a', encoding='utf-8') as log:
                    log.writelines(
                        f'[func_name: {func.__name__} — parameters:{arg} — type_error:{type(info)} — {info}]\n')
                    return 'Something wrong, check "Function_error.log"'

        return executer

    return function


# TODO здесь ваш код

# Проверить работу на следующих функциях

@log_errors(log_name='log_file.txt')
def perky(param):
    return param / 0


@log_errors(log_name='log_file.txt')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]

for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')

print(perky(42))


# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
