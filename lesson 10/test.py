from libs.exc_10_2 import IamGodError
try:

    raise IamGodError
except Exception as nme:

    print(f'ошибка - {nme.nam}')