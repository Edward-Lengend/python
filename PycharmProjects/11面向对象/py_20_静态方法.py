"""
静态方法特点
·需要通过装饰器@staticmethod来进行修饰，
    静态方法既不需要传递类对象也不需要传递实例对象（形参没有self/cls）。
·静态方法也能够通过实例对象和类对象去访问。

静态方法使用场景
·当方法中既不需要使用实例对象（如实例对象，实例属性），
    也不需要使用类对象（如类属性、类方法、创建实例等）时，定义静态方法
·取消不需要的参数传递，有利于减少不必要的内存占用和性能消耗
"""

# 1.定义类， 定义静态方法


class Dog(object):
    @staticmethod
    def print_info():
        print('这是一个静态方法')


# 2.创建对象
wangcai = Dog()

# 3.调用静态方法： 类和对象
wangcai.print_info()
Dog.print_info()