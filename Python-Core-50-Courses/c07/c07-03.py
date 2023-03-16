"""
《百钱百鸡》问题

Version: 0.1
Author: XXXX
"""
# 假设公鸡的数量为x，x的取值范围是0到20
for x in range(0, 21):
    # 假设母鸡的数量为y，y的取值范围是0到33
    for y in range(0, 34):
        z = 100 - x - y
        if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
            print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')