import itertools as itertools
import math as math
from time import sleep


@profile
def benchmark_func_with_factorial(replicates=1500):
    def primes_one():
        a = 1
        while True:
            a += 1
            if (math.factorial(a - 1) + 1) % a == 0:
                yield a

    [list(itertools.takewhile(lambda x: x <= i, primes_one())) for i in range(replicates)]
    sleep(1)
    return None


@profile
def benchmark_func_without_factorial(replicates=1500):
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

    [list(itertools.takewhile(lambda x: x <= i, primes_two())) for i in range(replicates)]
    sleep(1)
    return None


if __name__ == '__main__':
    benchmark_func_with_factorial()
    benchmark_func_without_factorial()
