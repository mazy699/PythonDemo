"""
数值类型
    整数类型
        表示整数数值，正整数，负数和0
        理论上取值范围[负无穷，正无穷]
        不可变数据类型
"""
num1 = 99  # 默认十进制
num2 = 0b1111  # 使用二进制表示整数
num3 = 0o77  # 使用八进制表示整数
num4 = 0xff  # 使用十六进制表示整数

print(num1)
print(num2)
print(num3)
print(num4)

"""
数值类型
    浮点数类型
        表示带有小数点的数值
        由整数部分和小数部分组成，必须带有小数部分，小数部分可以是0
        可以使用科学计数法表示
        两个浮点数运算，由一定概率运算结果后增加一些”不确定“尾数
        使用内置函数round()限定运算结果需要保留的小数位数
        不可变数据类型
"""
num5 = 10
num6 = 10.0
print(num5, type(num5))
print(num6, type(num6))
# 浮点数不确定尾数
print(0.1 + 0.2)
print(round(0.1 + 0.2, 1))  # 保留1位小数

"""
数值类型
    复数类型
        由实部和虚部组成，必须带有小数部分，小数部分可以是0
        j = √-1,（根号-1）是复数的一个基本单位，又称”虚数单位“
        .real 获取实数部分
        .imag 获取虚数部分
        不可变数据类型
"""
# 复数类型多见于科学计算中
num7 = 12 + 34j
print(num7.real)
print(num7.imag)

"""
字符串类型
    连续的字符序列，可以表示计算机能识别的一切字符
    不可变数据类型，即不可变字符序列
    单行字符串使用'......'或"......"
"""
# 多行字符串使用'''......'''或"""......"""

str1 = 'abc'
print(str1)

str2 = '''abc
123
def'''
print(str2)

# 转义字符\n改行
print('aaa\nbbb')

# 字符串索引
str3 = 'helloworld'
print(str3[0], str3[-10])  # 正向递增序号从0开始，反向递减序号从-1开始

# 字符串切片
print(str3[5:9])  # 正向递增序列，不包括9
print(str3[5:])  # 正向递增序列，从5开始到末尾
print(str3[-5:-1])  # 反向递减序列，不包括-1
print(str3[-5:])  # 反向递减序列，从-5开始到末尾

# 字符串类型的操作
# x+y 连接两个字符串
# x*n 复制n次字符串
# x in s 如果x是s的字串，结果为True，否则为False
print('ddd' + 'eee')
print('fff' * 3)
print('ab' in 'abcde')
print('ab' in 'cd')

"""
布尔类型
    用来表示真值或假值
    使用True和False表示布尔类型的值
    可转化为数值，True表示1，False表示0
    所有对象都有一个布尔值，使用内置函数bool()进行测试
    布尔值为假的情况
        False或者None
        数值中的0，包含0，0.0，虚数0
        空序列，包含空字符串，空数组，空列表，空字典
        自定义对象的实例，该对象的__bool__()方法返回False或者__len__()方法返回0
"""
x = True
print(x, type(x))
print(True + 10)  # 1+10
print(False + 10)  # 0+10
print(bool(12))
print(bool(0), bool(0.0))
print(bool('ss'))
print(bool(''))
print(bool(True))
print(bool(False))
print(bool(None))
