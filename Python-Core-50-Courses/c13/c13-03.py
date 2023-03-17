"""
参数的默认值

Version: 0.1
Author: 骆昊
"""
from random import randint


# 定义摇色子的函数，n表示色子的个数，默认值为2
def roll_dice(n=2):
    """摇色子返回总的点数"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


# 如果没有指定参数，那么n使用默认值2，表示摇两颗色子
print(roll_dice())
# 传入参数3，变量n被赋值为3，表示摇三颗色子获得点数
print(roll_dice(3))