class EventIterrator:
    def __init__(self, inpt):
        self.curr_time = ''
        self.event_counter = 0
        self.inpt = []
        for line in inpt:
            self.inpt.append(line[1:])
        self.inpt = list(filter(lambda string: string[28:31] == 'NOK', self.inpt))

    def __iter__(self):
        self.string_num = 0

        return self

    def __next__(self):
        try:
            if self.string_num >= len(self.inpt):
                raise StopIteration

            self.curr_time = self.inpt[self.string_num][0:16]
            self.event_counter = 1
            self.string_num += 1
            while self.curr_time == self.inpt[self.string_num][0:16]:
                self.event_counter += 1
                self.string_num += 1
                if self.string_num > len(self.inpt):
                    break
            return self.curr_time, self.event_counter

        except IndexError:
            return self.curr_time, self.event_counter
