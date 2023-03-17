def gcd_and_lcm(x: int, y: int) -> int:
    """求最大公约数和最小公倍数"""
    a, b = x, y
    while b % a != 0:
        a, b = b % a, a
    return a, x * y // a

def gcd(x: int, y: int) -> int:
    """求最大公约数"""
    while y % x != 0:
        x, y = y % x, x
    return x


def lcm(x: int, y: int) -> int:
    """求最小公倍数"""
    return x * y // gcd(x, y)

print(gcd_and_lcm(2,4))
print(gcd(2,4))
print(lcm(2,4))