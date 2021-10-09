# 在Python中，xx()的函数叫做魔法方法，指的是具有特殊功能的函数。

# __init__()

# 思考：洗衣机的宽度高度是与生俱来的属性，在创建对象之前就应该设置好

class Washer:
    def __init__(self):
        # 添加实例属性
        self.width = 50
        self.height = 100

    def print_info(self):
        print(f'height = {self.height}')
        print(f'width = {self.width}')


haier = Washer()
haier.print_info()