# 类： 洗衣机  功能： 洗衣服


class Washer:
    def wash(self):
        print('洗衣服')
        print(f'self = {self}')


haier = Washer()
print(haier)
haier.wash()

# 由于打印对象和打印se1f得到的内存地址相同
# 所以<self指的是调用该函数的对象>
