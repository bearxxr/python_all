import time


def now():
    print('2020-08-17')


f = now
# 打出函数的名字
print(now.__name__)
print(f.__name__)


# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def cal_time(fn):
    print('=====我被调用了')

    def inner():
        start = time.time()
        fn()
        end = time.time()
        print('%s函数执行花费了%s秒' % (fn.__name__, end - start))
    return inner


@cal_time
def print_hello():
    for i in range(1000):
        print('Hello World!')


print_hello()
