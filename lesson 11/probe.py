import time


def time_track(func):


    def surrogate(*args, **kwargs):
        try:
            started_at = time.time()

            result = func(*args, **kwargs)

            ended_at = time.time()
            elapsed = round(ended_at - started_at, 4)
            print(f'Функция работала {elapsed} секунд(ы)')
            return result


        except:
            return 'something wrong'

    return surrogate


def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))

# а можно вообще сделать так
digits = time_track(digits)
result = digits(3141, 5926, 2718, 2818)
print(result)