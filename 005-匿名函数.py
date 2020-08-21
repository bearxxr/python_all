a = lambda x: x ** 2

# print(list(map(a, [1, 2, 3, 4, 5])))
# next(map(a, [1, 2, 3, 4, 5]))

# 找出filter函数
L = type(list(filter(lambda x: x % 2 == 1, range(20))))
print(L)