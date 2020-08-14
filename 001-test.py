from collections.abc import Iterator
from functools import reduce


def f(x, y):
    return x * 10 + y


def fn(i):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[i]


a = map(fn, '12345')  # 等待调用
b = reduce(f, a)
print(b)

# 即
c = reduce(f, map(fn, '45678'))
print(c)

# map对象就是迭代器类型
print(isinstance(a, Iterator))


def cal(arg):
    for i in arg:
        return i[1]


a = (['a', 98], ['b', 99], ['c', 100])
print(cal(a))
