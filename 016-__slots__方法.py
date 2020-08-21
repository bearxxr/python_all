class Animal:
    __slots__ = ['age', 'score']


a = Animal()
a.age = 78
print(a.age)


# a.color = 'red'
# print(a.color)

class Dog(Animal):
    pass


# __slots__只对当前类的实例有用，对继承了当前类的类及其实例对象都无效
d = Dog()
d.color = 'red'
print(d.color)
