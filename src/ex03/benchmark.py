#!/usr/bin/env python3

import timeit
import sys
from functools import reduce

class Benchmark:
    def __init__(self):
        pass

    def loop_numbers(self, num):
        i = 0
        sum = 0
        while i <= num:
            sum = sum + i*i
            i += 1
        return sum

    def reduce_numbers(self, num):
        result = reduce(lambda x, y: x + y*y , range(1, num + 1),0)
        return result


if __name__ == '__main__':
    benchmark = Benchmark()

    function_name = sys.argv[1]
    function_count = int(sys.argv[2])
    number = int(sys.argv[3])

    cycle_time = timeit.timeit(lambda: benchmark.loop_numbers(number))
    reduce_time = timeit.timeit(lambda: benchmark.reduce_numbers(number))

    if function_name == 'loop':
        print(cycle_time)
    elif function_name == 'reduce':
        print(reduce_time)

