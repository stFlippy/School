import logging
from logging import Formatter



class VsePoJope(Exception):

    def __str__(self):
        return "Чекни входные данные"


class BowlCntr:
    def __init__(self, name):
        self.name = name
        self.game_result = ""
        self.cnt = 0

    def get_score(self, inpt):
        self.game_result = inpt

        log.info('hmmmm....info')
        log.debug('hmmmm....debug')
        log.warning('hmmmm....warn')
        log.error('hmmmm....error')

        for i, symbol in enumerate(self.game_result):
            # try:



            if symbol.isdigit():
                self.cnt += int(symbol)
                continue

            if symbol.upper() == "X":
                self.cnt += 20
                continue

            if symbol == "/":
                self.cnt = self.cnt - int(self.game_result[i - 1]) + 15
                continue

            else:
                raise VsePoJope

        # except Exception as exc:
        #     raise VsePoJope

        return self.cnt


if __name__ == '__main__':
    log = logging.getLogger('__name__')
    log.setLevel(logging.DEBUG)
    shell_handler = logging.StreamHandler()
    shell_handler.setLevel('WARNING')
    shell_handler.setFormatter(Formatter(fmt = '%(asctime)s     %(funcName)s    %(levelname)s:%(name)s:%(message)s'))
    log.addHandler(shell_handler)

    baton = BowlCntr("baton")
    print(baton.get_score("1/134"))
