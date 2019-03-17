def RangeGenerator(*args):
    """
    Return an object that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.  RangeGenerator(i, j) produces i, i+1, i+2, ..., j-1.
    start defaults to 0, and stop is omitted!  RangeGenerator(4) produces 0, 1, 2, 3.
    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement).
    Examples:
    [i for i in RangeGenerator(3)] #stop is 3
    >[0, 1, 2]
    [i for i in RangeGenerator(1, 3)] #start is 1, stop is 3
    >[1, 2]
    [i for i in RangeGenerator(3, 7, 2)] #start is 3, stop is 7, step is 2
    >[3, 5]
    [i for i in RangeGenerator(*{3: 3})] #stop is 3
    >[0, 1, 2]
    """
    if (len(args) == 0) or (len(args) > 3):
        raise TypeError("RangeGenerator expected 1, 2 or 3 arguments, got {}".format(len(args)))
    start = 0 if len(args) < 2 else args[0]
    stop = args[0] if len(args) == 1 else args[1]
    step = 1 if len(args) < 3 else args[2]
    if (type(start) is not int) or (type(stop) is not int) or (type(step) is not int):
        raise TypeError("object cannot be interpreted as an integer")
    if not step:
        raise ValueError("RangeGenerator() arg 3 must not be zero")

    if (start < stop) and step > 0:
        while start < stop:
            answer = start
            start += step
            yield answer
    elif (start > stop) and step < 0:
        while start > stop:
            answer = start
            start += step
            yield answer
