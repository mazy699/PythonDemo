s = 'hello, world'

# center方法以宽度20将字符串居中并在两侧填充*
print(s.center(20, '*'))  # ****hello, world****
# rjust方法以宽度20将字符串右对齐并在左侧填充空格
print(s.rjust(20))        #         hello, world
# ljust方法以宽度20将字符串左对齐并在右侧填充~
print(s.ljust(20, '~'))   # hello, world~~~~~~~~
# 在字符串的左侧补零
print('33'.zfill(5))      # 00033
print('-33'.zfill(5))     # -0033

print('--------------------------')
a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))

print('--------------------------')
a = 321
b = 123
print('{0} * {1} = {2}'.format(a, b, a * b))

print('--------------------------')
a = 321
b = 123
print(f'{a} * {b} = {a * b}')