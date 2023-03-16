"""
猜数字游戏

Version: 0.1
Author: XXXX
"""
import random

# 产生一个1-100范围的随机数
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
# 当退出while循环的时候显示用户一共猜了多少次
print(f'你总共猜了{counter}次')