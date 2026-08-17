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


if __name__ == '__main__':
    benchmark = Benchmark()
    cycle_time = timeit.timeit(lambda: benchmark.cycle_method(emails), number=9000000)
    list_time = timeit.timeit(lambda: benchmark.list_method(emails), number=9000000)

    if cycle_time > list_time:
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a cycle")

    print(f"{cycle_time} vs {list_time}")