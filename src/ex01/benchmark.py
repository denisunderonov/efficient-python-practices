from config import emails
import timeit

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


if __name__ == '__main__':
    benchmark = Benchmark()
    cycle_time = timeit.timeit(lambda: benchmark.cycle_method(emails), number=900000)
    list_time = timeit.timeit(lambda: benchmark.list_method(emails), number=900000)
    map_time = timeit.timeit(lambda: benchmark.map_method(emails), number=900000)

    times = []
    times.extend((cycle_time, list_time, map_time))
    min_time = min(times)
    times.remove(min_time)
    mid_time = min(times)
    times.remove(mid_time)
    max_time = times[0]

    if min_time == cycle_time:
        print("it is better to use a cycle")
    elif min_time == list_time:
        print("it is better to use a list comprehension")
    elif min_time == map_time:
        print("it is better to use a map")


    print(f"{min_time} vs {mid_time} vs {max_time}")