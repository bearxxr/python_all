class Animal:
    def run(self):
        print('我是一个动物')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
dog.run()