class Triangle(object):
    """三角形类"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    # @classmethod
    # def is_valid(cls, a, b, c):
    #     """判断三条边长能否构成三角形(类方法)"""
    #     return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


if Triangle.is_valid(2, 3, 5):
    print(Triangle.perimeter(Triangle(2, 3, 5)))
else:
    print('不是三角形')
print('---------------------')
if Triangle.is_valid(2, 3, 4):
    print(Triangle.perimeter(Triangle(2, 3, 4)))
else:
    print('不是三角形')
