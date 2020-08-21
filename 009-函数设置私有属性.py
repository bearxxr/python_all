# 函数设置私有属性的方法，函数名字前面加上双下划线__,就不能直接调用了


class Student:
    def __init__(self, score, gender):
        self.score = score
        self.__gender = gender

    def get_gender(self):
        return self.__gender


bear = Student(99, 'male')
# 这个不能访问的原因是因为，python 解释器把__gender变成了_Student__gender属性
# print(bear._gender)

print(bear.get_gender())
