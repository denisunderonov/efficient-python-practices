#!/usr/bin/env python3

import sys
import resource

def read_file(fname):
    with open(fname, "r", encoding="utf-8") as file:
        result = []
        for line in file:
            result.append(line)
        return result

if __name__ == '__main__':
    mas = read_file(sys.argv[1])
    for line in mas:
        pass

    
    usage = resource.getrusage(resource.RUSAGE_SELF)

    # На macOS ru_maxrss измеряется в байтах
    memory_gb = usage.ru_maxrss / (1024 ** 3)

    # Процессорное время программы
    total_time = usage.ru_utime + usage.ru_stime

    print(f"Peak Memory Usage = {memory_gb:.3f} GB")
    print(f"User Mode Time + System Mode Time = {total_time:.2f}s")