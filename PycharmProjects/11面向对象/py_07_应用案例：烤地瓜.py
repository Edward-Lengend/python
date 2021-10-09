"""
需求主线：
1.被烤的时间和对应的地瓜状态：
0-3分钟：生的
3-5分钟：半生不熟
5-8分钟：熟的
超过8分钟：烤糊了
2.添加的调料：
用户可以按自己的意愿添加调料
"""


class SweetPotato:
    def __init__(self):
        # 被烤时间
        self.time = 0
        # 地瓜状态
        self.state = '生的'
        # 调料列表
        self.seasonings = []

    def __str__(self):
        return f'这个地瓜烤了{self.time}分钟， 是个{self.state}地瓜'

    def cook(self, time):
        self.time += time
        if self.time < 0:
            print('请输入正确的时间')
        if 0 <= self.time <= 3:
            self.state = '生'
        elif 3 < self.time <= 5:
            self.state = '半生'
        elif 5 < self.time <= 8:
            self.state = '熟'
        else:
            self.state = '糊'

        print(f'你得到了一个{self.state}的地瓜')

    # def add_seasoning(self, seasonings):



WhiteSweetPotato = SweetPotato()

WhiteSweetPotato.cook(1)
print(WhiteSweetPotato)
WhiteSweetPotato.cook(2)
print(WhiteSweetPotato)
WhiteSweetPotato.cook(2)
print(WhiteSweetPotato)
WhiteSweetPotato.cook(3)
print(WhiteSweetPotato)
WhiteSweetPotato.cook(2)
print(WhiteSweetPotato)


