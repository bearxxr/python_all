class Student:
    name = 'Bear'


bear = Student()
print(bear.name)
print(Student.name)

bear.name = 'molica'
print(bear.name)


del bear.name
print(bear.name)