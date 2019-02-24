class MassiveIterator:
    def __init__(self, massive, start=0, step=1):
        if (len(massive) == 0) or (len(massive) > 3):
            raise TypeError("massive iterator expected 1, 2 or 3 arguments, got {}".format(len(massive)))
        elif len(massive) == 1:
            self.start, self.stop, self.step = start, massive[0], step
        elif len(massive) == 2:
            self.start, self.stop, self.step = massive[0], massive[1], step
        else:
            self.start, self.stop, self.step = massive[0], massive[1], massive[2]

    def __iter__(self):
        return MyIterator(self.start, self.stop, self.step)


class MyIterator:
    def __init__(self, start, stop, step):
        self.start, self.stop, self.step = start, stop, step

    def __next__(self):
        if (self.start < self.stop) and self.step > 0:
            while self.start < self.stop:
                answer = self.start
                self.start += self.step
                return answer
            raise StopIteration
        elif (self.start > self.stop) and self.step < 0:
            while self.start > self.stop:
                answer = self.start
                self.start += self.step
                return answer
            raise StopIteration
        else:
            raise StopIteration
