class Student:

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('这不是整数呀！')
        if value < 0 or value > 100:
            raise ValueError('必须在0~100之间')
        self._score = value


s = Student()
s.name = 'bear'
print(s.name)

s2 = Student()
s2.set_score(100)
print(s2.get_score())




