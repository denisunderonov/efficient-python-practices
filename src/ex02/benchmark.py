#!/usr/bin/env python3

from config import emails
import timeit
import sys

class Benchmark:
    def __init__(self):
        self.gmail = '@gmail.com'

    def cycle_method(self, emails):
        result = []
        for email in emails:
            if self.gmail in email:
                result.append(email)
        return result

    def list_method(self, emails):
        result = [email for email in emails if self.gmail in email]
        return result

    def map_method(self, emails):
        def gmail(email):
            if self.gmail in email:
                return email
        
        result = list(map(gmail,emails))
        return result

    def filter_method(self, emails):
        def gmail(email):
            if self.gmail in email:
                return email

        result = list(filter(gmail, emails))
        return result
        

if __name__ == '__main__':
    benchmark = Benchmark()

    function_name = sys.argv[1]
    function_count = int(sys.argv[2])

    cycle_time = timeit.timeit(lambda: benchmark.cycle_method(emails), number=function_count)
    list_time = timeit.timeit(lambda: benchmark.list_method(emails), number=function_count)
    map_time = timeit.timeit(lambda: benchmark.map_method(emails), number=function_count)
    filter_time = timeit.timeit(lambda: benchmark.filter_method(emails), number=function_count)

    if function_name == 'loop':
        print(cycle_time)
    elif function_name == 'list_comprehension':
        print(list_time)
    elif function_name == 'map':
        print(map_time)
    elif function_name == 'filter':
        print(filter_time)
