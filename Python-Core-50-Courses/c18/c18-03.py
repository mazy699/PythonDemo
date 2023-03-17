class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
# 为Student对象动态添加sex属性
stu.sex = '男'