s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2, s1 < s2)      # False True
print(s2 == 'hello world')    # True
print(s2 == 'Hello world')    # False
print(s2 != 'Hello world')    # True
s3 = '骆昊'
print(ord('骆'), ord('昊'))               # 39558 26122
s4 = '王大锤'
print(ord('王'), ord('大'), ord('锤'))    # 29579 22823 38180
print(s3 > s4, s3 <= s4)      # True False

print('-----------------------')
s1 = 'hello world'
s2 = 'hello world'
s3 = s2
# 比较字符串的内容
print(s1 == s2, s2 == s3)    # True True
# 比较字符串的内存地址
print(s1 is s2, s2 is s3)    # False True