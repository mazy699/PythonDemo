class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 属性访问器(getter方法) - 获取__name属性
    @property
    def name(self):
        return self.__name
    
    # 属性修改器(setter方法) - 修改__name属性
    @name.setter
    def name(self, name):
        # 如果name参数不为空就赋值给对象的__name属性
        # 否则将__name属性赋值为'无名氏'，有两种写法
        # self.__name = name if name else '无名氏'
        self.__name = name or '无名氏'
    
    @property
    def age(self):
        return self.__age


stu = Student('王大锤', 20)
print(stu.name, stu.age)    # 王大锤 20
stu.name = ''
print(stu.name)    # 无名氏
# stu.age = 30     # AttributeError: can't set attribute