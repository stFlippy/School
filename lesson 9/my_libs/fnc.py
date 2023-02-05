from pprint import pprint


class InputData:

    def __init__(self, file_name):
        self.arr = []
        self.dct = {}
        self.grp_dct = {}
        with open(file_name, 'r') as in_data:
            for strs in in_data:
                self.arr.append(strs)

    def __str__(self):
        pass

    def prt(self, intgr):
        pprint(self.grp_dct)
        intgr += 1

    def check(self):
        time = Time()
        for strs in self.arr:
            if strs[29: 32] == 'NOK':
                time.calculate(strs[1:20])
                fltred_time = f'[{time.yr}-{time.mon}-{time.day} {time.hr}:{time.min}]'
                if fltred_time in self.dct:
                    self.dct[fltred_time] += 1
                else:
                    self.dct[fltred_time] = 1

    def grp_hr(self):
        time = Time()

        for itm in self.dct:
            time.calculate(itm[1:])
            if time.hr not in self.grp_dct:
                self.grp_dct[time.hr] = {itm: self.dct[itm]}
            else:
                self.grp_dct[time.hr].update({itm: self.dct[itm]})

    def grp_day(self):
        pass

    def grp_mnth(self):
        pass


class Time:

    def __init__(self):
        self.day = 0
        self.mon = 0
        self.yr = 0
        self.hr = 0
        self.min = 0
        self.sec = 0

    def calculate(self, inpt):
        self.day = (inpt[8: 10])
        self.mon = (inpt[5: 7])
        self.yr = (inpt[0: 4])
        self.hr = (inpt[11: 13])
        self.min = (inpt[14: 16])
        if inpt[17: 21]:
            self.sec = (inpt[17: 21])
