s = '   jackfrued@126.com  \t\r\n'
# strip方法获得字符串修剪左右两侧空格之后的字符串
print(s.strip())    # jackfrued@126.com

print('-------------------------')
s = 'hello, world'
print(s.replace('o', '@'))     # hell@, w@rld
print(s.replace('o', '@', 1))  # hell@, world

print('-------------------------')
s = 'I love you'
words = s.split()
print(words)            # ['I', 'love', 'you']
print('#'.join(words))  # I#love#you

print('-------------------------')
s = 'I#love#you#so#much'
words = s.split('#')
print(words)  # ['I', 'love', 'you', 'so', 'much']
words = s.split('#', 3)
print(words)  # ['I', 'love', 'you', 'so#much']

print('-------------------------')
a = '骆昊'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b, c)  # b'\xe9\xaa\x86\xe6\x98\x8a' b'\xc2\xe6\xea\xbb'
print(b.decode('utf-8'))
print(c.decode('gbk'))