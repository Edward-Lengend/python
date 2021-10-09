

class Washer:
    def wash(self):
        print('洗衣服')
    # 类中获取对象属性
    def print_info(self):
        print(f'haier.height = {haier.height}')
        print(f'haier.width = {haier.width}')


# 添加属性
# 对象名.属性名 = 值
haier = Washer()
haier.height = 100
haier.width = 50


# 获取属性
print(f'冰箱高度为{haier.height}, 冰箱宽度为{haier.width}')

haier.print_info()