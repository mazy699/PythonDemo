"""
python是一种动态类型的语言，变量的类型可以随时变化
    使用内置函数type()可以查看变量的数据类型
允许多个变量指向同一个值
    使用内置函数id()可以返回变量所指的内存地址
"""
num = 1
print(num)
print(type(num))
num = 'a'
print(num)
print(type(num))

number = num = 10
print(num, number)
print(type(num), type(num))
print(id(num), id(num))
