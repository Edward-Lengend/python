class Master:
    def __init__(self):
        self.kongfu = 'Master煎饼果子技术'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class School(Master):
    def __init__(self):
        self.kongfu = 'School马煎饼果子技术'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
    # 2.1  super带参数写法
        super(School, self).__init__()
        super(School, self).make_cake()

class Prentice(School):
    def __init__(self):
        self.kongfu = '独创'

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 需求：一次性调用父类School, Master的方法
    # 方法一： 调用父类方法，必须进行初始化
    # 如果定义的类名进行更改， 这里也要修改， 麻烦， 代码量大
    """
     def make_old_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
        School.__init__(self)
        School.make_cake(self)
    """

    # 方法二：super()
    # 2.1 super(当前类名， self).函数
    """
        def make_old_cake(self):
        # 调用School类的方法
        super(Prentice, self).__init__()
        super(Prentice, self).make_cake()

    """
    # 2.2  super().函数
    def make_old_cake(self):
        # 调用School类的方法
        super().__init__()
        super().make_cake()



zhang = Prentice()
zhang.make_old_cake()

#总结： super遵循__mro__顺序自动向上寻找父类， 适合单继承的时候使用