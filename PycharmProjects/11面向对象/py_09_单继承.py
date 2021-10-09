"""
故事主线：一个煎饼果子老师傅，在煎饼果子界摸爬滚打多年，
研发了一套精湛的摊煎饼果子的技术。师父要把这套技术传授给他的唯一的最得意的徒弟。
"""


class Master:
    def __init__(self):
        self.kongfu = "古法煎饼果子配方"

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class Prentice(Master):
    pass


prentice = Prentice()
prentice.make_cake()