def MassiveGenerator(massive, start=0, step=1):
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
