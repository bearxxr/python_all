class Animal:

    def __init__(self):
        self.x = 1
        self.y = 2

    def run(self):
        print("I'm a animal")


dog = Animal()

print(hasattr(dog, 'x'))
print(getattr(dog, 'x'))
setattr(dog, 'z',999)
print(dog.z)