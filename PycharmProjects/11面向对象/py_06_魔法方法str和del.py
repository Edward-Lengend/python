"""
当使用print输出对象的时候，默认打印对象的内存地址
如果类定义了str_方法，那么就会打印从在这个方法中return的数据。
"""


class Washer:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        # 可以放对象或类的说明， 打印对象就不再是地址
        return '洗衣机'

    def __del__(self):
        print(f'{self}对象被删除')


instruction = Washer(50, 100)
print(instruction)

del instruction
