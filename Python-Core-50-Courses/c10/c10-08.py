s = 'hello, world!'

# find方法从字符串中查找另一个字符串所在的位置
# 找到了返回字符串中另一个字符串首字符的索引
print(s.find('or'))        # 8
# 找不到返回-1
print(s.find('shit'))      # -1
# index方法与find方法类似
# 找到了返回字符串中另一个字符串首字符的索引
print(s.index('or'))       # 8
# 找不到引发异常
#print(s.index('shit'))     # ValueError: substring not found

print('-----------------------')
s = 'hello good world!'

# 从前向后查找字符o出现的位置(相当于第一次出现)
print(s.find('o'))       # 4
# 从索引为5的位置开始查找字符o出现的位置
print(s.find('o', 5))    # 7
# 从后向前查找字符o出现的位置(相当于最后一次出现)
print(s.rfind('o'))      # 12