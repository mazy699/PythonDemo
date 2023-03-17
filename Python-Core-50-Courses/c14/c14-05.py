import math


def ptp(data):
    """求极差（全距）"""
    return max(data) - min(data)


def average(data):
    """求均值"""
    return sum(data) / len(data)


def variance(data):
    """求方差"""
    x_bar = average(data)
    temp = [(num - x_bar) ** 2 for num in data]
    return sum(temp) / (len(temp) - 1)


def standard_deviation(data):
    """求标准差"""
    return math.sqrt(variance(data))


def median(data):
    """找中位数"""
    temp, size = sorted(data), len(data)
    if size % 2 != 0:
        return temp[size // 2]
    else:
        return average(temp[size // 2 - 1:size // 2 + 1])