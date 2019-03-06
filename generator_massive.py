def MassiveGenerator(massive, start=0, step=1):
    """
    Massive can be a list with 1, 2 or 3 values. There are 3 arguments: massive (stop), start, step.
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
    if (len(massive) == 0) or (len(massive) > 3):
        raise TypeError("massive generator expected 1, 2 or 3 arguments, got {}".format(len(massive)))
    elif len(massive) == 1:
        stop = massive[0]
    elif len(massive) == 2:
        start, stop = massive[0], massive[1]
    else:
        start, stop, step = massive[0], massive[1], massive[2]
    return MyGenerator(start, stop, step)


def MyGenerator(start, stop, step):
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
