
class bowl_cntr:
    def __init__(self):
        self.game_result = ""
        self.cnt = 0

    def get_score(self, inpt):
        self.game_result = inpt

        for i, chr in enumerate(self.game_result):
            if chr.isdigit:
                self.cnt += int(chr)
                continue

            if chr.upper == "X":
                self.cnt += 20
                continue

            if chr == "/":
                self.cnt = self.cnt - int(self.game_result[i - 1]) + 15
                continue

            else:
                raise Exception