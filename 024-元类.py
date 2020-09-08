def fn(x):
    return "Hello World"


# type创建一个类时需要在方法中加一个参数
Hello = type('Hello', (object,), {'hello': fn})

a = Hello()
print(type(a))
print(a.hello())



