s1 = 'hello, world!'
s2 = "你好，世界！"
print(s1, s2)
# 以三个双引号或单引号开头的字符串可以折行
s3 = '''
hello, 
world!
'''
print(s3, end='')

print('-------------------')
s1 = '\'hello, world!\''
print(s1)
s2 = '\\hello, world!\\'
print(s2)

print('-------------------')
# 字符串s1中\t是制表符，\n是换行符
s1 = '\time up \now'
print(s1)
# 字符串s2中没有转义字符，每个字符都是原始含义
s2 = r'\time up \now'
print(s2)

print('-------------------')
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)

print('-------------------')
s1 = 'hello' + ' ' + 'world'
print(s1)    # hello world
s2 = '!' * 3
print(s2)    # !!!
s1 += s2     # s1 = s1 + s2
print(s1)    # hello world!!!
s1 *= 2      # s1 = s1 * 2
print(s1)    # hello world!!!hello world!!!