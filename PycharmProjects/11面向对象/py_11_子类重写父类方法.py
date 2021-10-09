class Master:
    def __init__(self):
        self.kongfu = '古法煎饼果子技术'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class School:
    def __init__(self):
        self.kongfu = '黑马煎饼果子技术'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class Prentice(Master, School):
    def __init__(self):
        self.kongfu = '独创'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

xiaoming = Prentice()
xiaoming.make_cake()

# 查看继承顺序
print(Prentice.__mro__)