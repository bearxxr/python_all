class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __getattr__(self, arg):
        if arg == 'age':
            return 99


s = Student('bear')
print(s.xx)


# 返回函数
class Animal:
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25


a = Animal()
print(a.age())