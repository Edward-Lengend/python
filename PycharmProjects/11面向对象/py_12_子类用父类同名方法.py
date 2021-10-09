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
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 调用父类方法，必须进行初始化
    def make_Master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_School_cake(self):
        School.__init__(self)
        School.make_cake(self)


zhang = Prentice()
zhang.make_cake()
zhang.make_Master_cake()
zhang.make_School_cake()
