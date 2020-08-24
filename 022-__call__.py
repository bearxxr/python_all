# 直接调用实例对象


class Human(object):

    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        return "My Name Is %s" % self.name

    def __repr__(self):
        return self.name


h = Human('bear')
print(h())

# 查看对象是否能被调用
print(callable(h))
print(callable([1, 2]))
print(callable(bool))
