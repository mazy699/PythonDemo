# 定义一个三元组
t1 = (30, 10, 55)
# 定义一个四元组
t2 = ('骆昊', 40, True, '四川成都')

# 查看变量的类型
print(type(t1), type(t2))    # <class 'tuple'> <class 'tuple'>
# 查看元组中元素的数量
print(len(t1), len(t2))      # 3 4

# 通过索引运算获取元组中的元素
print(t1[0], t1[-3])         # 30 30
print(t2[3], t2[-1])         # 四川成都 四川成都

# 循环遍历元组中的元素
for member in t2:
    print(member)

# 成员运算
print(100 in t1)    # False
print(40 in t2)     # True

# 拼接
t3 = t1 + t2
print(t3)           # (30, 10, 55, '骆昊', 40, True, '四川成都')

# 切片
print(t3[::3])      # (30, '骆昊', '四川成都')

# 比较运算
print(t1 == t3)    # False
print(t1 >= t3)    # False
print(t1 < (30, 11, 55))    # True

print('----------------')
# 空元组
a = ()
print(type(a))    # <class 'tuple'>
# 不是元组
b = ('hello')
print(type(b))    # <class 'str'>
c = (100)
print(type(c))    # <class 'int'>
# 一元组
d = ('hello', )
print(type(d))    # <class 'tuple'>
e = (100, )
print(type(e))    # <class 'tuple'>