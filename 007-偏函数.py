a = '12345'
b = int(a)

print(b)
print(type(b))

c = int(a, base=8)
print(c)
d = int(a, base=6)
# print(d)

# 偏函数，构造一个新函数
import functools

int2 = functools.partial(int, base=2)

f = int2('1001')
print(f)

