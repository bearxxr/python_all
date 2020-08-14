from collections.abc import Iterator


def f(x):
    if x / 2 == 0.5:
        return x


# filter()函数的返回值也是一个迭代器
a = filter(f, range(1000))
print(isinstance(a, Iterator))
for i in a:
    print(i)

