def fn():
    print('Hello World!')


Hello = type('Hello', (object,), dict(hello=fn))
a = Hello()
print(type(a))
a.hello()
