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
    pass

xiaoming = Prentice()
xiaoming.make_cake()