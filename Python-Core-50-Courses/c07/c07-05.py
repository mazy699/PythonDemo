"""
输出斐波那契数列前20个数

Version: 0.1
Author: XXXX
"""

a, b = 0, 1
for _ in range(20):
    a, b = b, a + b
    print(a)