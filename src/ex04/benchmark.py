#!/usr/bin/env python3
import random
from collections import Counter
import timeit

class Benchmark:
    def __init__(self):
        pass

    def generate_list(self):
        result = [random.randint(0,100) for _ in range(1000000)]
        return result

    def generate_dict(self, numbers):
        counts = {number: 0 for number in range(101)}

        for number in numbers:
            counts[number] += 1

        return counts

    def top_10(self, dictionary):
        sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
        i = 0
        for key in sorted_dict:
            if i > 10:
                break
            
            i += 1
            # print(key)

    def generate_dict_with_counter(self, numbers):
        counts = Counter(numbers)
        return counts

    def top_10_with_counter(self, dictionary):
        return dictionary.most_common(10)
            
if __name__ == '__main__':
    benchmark = Benchmark()

    my_list = benchmark.generate_list()

    my_function_time = timeit.timeit(lambda: benchmark.generate_dict(my_list), number=1)
    counter_time = timeit.timeit(lambda: benchmark.generate_dict_with_counter(my_list), number=1)

    my_top_time = timeit.timeit(lambda: benchmark.top_10(benchmark.generate_dict(my_list)), number=1)
    counter_top_time = timeit.timeit(lambda: benchmark.top_10_with_counter(benchmark.generate_dict_with_counter(my_list)), number=1)

    print(f"my function: {my_function_time}")
    print(f"Counter: {counter_time}")
    print(f"my top: {my_top_time}")
    print(f"Counter' s top: {counter_top_time}")
    

