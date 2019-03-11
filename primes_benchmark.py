import itertools as itertools
import math as math
from time import time
from random import randint


def benchmark_function_time(defined_function, replicates=1000):
    """
    This is a function which can be used for microbenchmarking of primes number generator
    :return: dictionary with function name, function average time of works and number of replicates
    """
    benchmark_info = {'function_name': defined_function.__name__, 'average_time': 0, 'replicates': replicates}
    for _ in range(replicates):
        i = randint(900, 1000)
        time_before_function = time()
        list(itertools.takewhile(lambda x: x <= i, defined_function()))
        time_after_function = time()
        time_diff = time_after_function - time_before_function
        benchmark_info["average_time"] += time_diff
    benchmark_info["average_time"] = benchmark_info["average_time"] / replicates
    return benchmark_info


def primes_one():
    a = 1
    while True:
        a += 1
        if (math.factorial(a - 1) + 1) % a == 0:
            yield a


def primes_two():
    i = 1
    while True:
        count = 0
        if i <= 2:
            i += 1
        else:
            i += 2
        for k in range(2, int(i ** 0.5) + 1):
            if i % k == 0:
                count += 1
                break
        if count == 0:
            yield i


print(benchmark_function_time(primes_one))
print(benchmark_function_time(primes_two))
