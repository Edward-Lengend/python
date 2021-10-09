"""
类属性就是类对象所拥有的属性，它被该类的所有实例对象所共有。
类属性可以使用类对象或实例对象访问。

类属性的优点
·记录的某项数据始终保持一致时，则定义类属性。
·实例属性要求每个对象为其单独开辟一份内存空间来记录数据，
    而类属性为全类所共有，仅占用一份内存，更加节省内存空间。
"""
# 1.定义类， 定义类属性
class Dog(object):
    tooth = 10


# 2.创建对象
wangcai = Dog()
xiaoqi = Dog()

# 3.访问类属性和类对象
print(Dog.tooth)  # 类属性可以通过类访问

print(wangcai.tooth)
print(xiaoqi.tooth)  # 类属性可以通过对象访问

# 4.修改类属性
"""
类属性只能通过类对象修改，不能通过实例对象修改
如果通过实例对象修改类属性，表示的是创建了一个实例属性。
"""
Dog.tooth = 20
print(f'Dog.tooth = {Dog.tooth}')
xiaoqi.tooth = 30
print(f'Dog.tooth = {Dog.tooth}')
print(f'xiaoqi.tooth = {xiaoqi.tooth}')  # 实例属性屏蔽类属性， 是新创建的属性
print(f'wangcai.tooth = {wangcai.tooth}')  # 修改一个实例属性， 其他实例属性不变
