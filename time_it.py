import timeit
import time

test_code = '''
for i in range(30):
    a = 100000**i
'''

print(timeit.timeit(stmt=test_code, number=10_000))

original_time = time.time()
for _ in range(10_000):
    for i in range(30):
        a = 100000**i
final_time = time.time()
print('time spent=', final_time - original_time)

original_time = timeit.default_timer()
for _ in range(10_000):
    for i in range(30):
        a = 100000**i
final_time = time.time()
print('time spent timeit=', timeit.default_timer() - original_time)

def test():
    for i in range(30):
        a = 10_000**i


print(timeit.timeit("test()", setup="from __main__ import test"))
