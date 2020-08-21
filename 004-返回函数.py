def fn_sum(args):
    def fn():
        a = 0
        for n in args:
            a = a + n
        return a

    return fn


x = fn_sum([1, 3, 4, 5, 6])
# print(x())
a = fn_sum(1)
b = fn_sum(1)

print(a == b)


# 返回函数闭包
def wrapper():
    _list = []
    for i in range(1, 4):
        def inner():
            return i * i

        _list.append(inner)

    return _list


f1, f2, f3 = wrapper()
print(f1())

print(type(range(4)))


def wrapper():
    def inner(j):
        def out():
            return j * j

        return out

    a = []
    for i in range(3):
        a.append(inner(i))
    return a


f1, f2, f3 = wrapper()
print(f1(), f2(), f3())
