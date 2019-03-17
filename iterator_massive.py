class RangeIterator:
    """
    Return an object that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.  RangeIterator(i, j) produces i, i+1, i+2, ..., j-1.
    start defaults to 0, and stop is omitted!  RangeIterator(4) produces 0, 1, 2, 3.
    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement).
    Examples:
    [i for i in RangeIterator(3)] #stop is 3
    >[0, 1, 2]
    [i for i in RangeIterator(1, 3)] #start is 1, stop is 3
    >[1, 2]
    [i for i in RangeIterator(3, 7, 2)] #start is 3, stop is 7, step is 2
    >[3, 5]
    [i for i in RangeIterator(*{3: 3})] #stop is 3
    >[0, 1, 2]
    """

    def __init__(self, *args):
        if (len(args) == 0) or (len(args) > 3):
            raise TypeError("RangeIterator expected 1, 2 or 3 arguments, got {}".format(len(args)))
        self.start = 0 if len(args) < 2 else args[0]
        self.stop = args[0] if len(args) == 1 else args[1]
        self.step = 1 if len(args) < 3 else args[2]
        if (type(self.start) is not int) or (type(self.stop) is not int) or (type(self.step) is not int):
            raise TypeError("object cannot be interpreted as an integer")
        if not self.step:
            raise ValueError("RangeIterator() arg 3 must not be zero")

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