"""
打印乘法口诀表

Version: 0.1
Author: XXXX
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end='\t')
    print()