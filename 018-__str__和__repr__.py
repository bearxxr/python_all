class Student:
    def __init__(self, name):
        self.name = name

    # 实例化时返回self.name
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


print(Student('bear'))

s = Student('susan')
print(s)
