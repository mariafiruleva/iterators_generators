from random import randint


class MassiveIterator:
    """
    Massive can be a list with 1, 2 or 3 values. There are 3 arguments: massive (analogue of "stop" argument in range
    function), start, step.
    By default, start = 0 and step = 1, but you can change it using more than one arguments.
    Examples:
    [i for i in MassiveIterator([3])] #stop is 3
    >[0, 1, 2]
    [i for i in MassiveIterator([1, 3])] #start is 1, stop is 3
    >[1, 2]
    [i for i in MassiveIterator([3, 7, 2])] #start is 3, stop is 7, step is 2
    >[3, 5]
    [i for i in MassiveIterator([*{3: 3}])] #stop is 3
    >[0, 1, 2]
    """

    def __init__(self, massive, start=0, step=1):
        if (len(massive) == 0) or (len(massive) > 3):
            raise TypeError("massive iterator expected 1, 2 or 3 arguments, got {}".format(len(massive)))
        elif len(massive) == 1:
            self.start, self.stop, self.step = start, massive[0], step
        elif len(massive) == 2:
            self.start, self.stop, self.step = massive[0], massive[1], step
        else:
            self.start, self.stop, self.step = massive[0], massive[1], massive[2]
        if (type(self.start) is not int) or (type(self.stop) is not int) or (type(self.step) is not int):
            raise TypeError("object cannot be interpreted as an integer")

    def __iter__(self):
        return self

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
