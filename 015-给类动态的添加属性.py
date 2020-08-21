class Student:
    pass


a = Student()
a.score = 99
print(a.score)


def set_attr(self, age):
    self.age = age


from types import MethodType

a.set_attr = MethodType(set_attr, a)

a.set_attr(25)
print(a.age)

a2 = Student()
# a2.set_attr(99)
# print(a2.age)
# AttributeError: 'Student' object has no attribute 'set_attr'
# MethodType只能给一个实例作用，不能给另一个实例使用

# 给类一个属性，所有的属性都可以使用
Student.set_attr = set_attr
a3 = Student()
a3.set_attr(999)
print(a3.age)
