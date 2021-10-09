"""
需要用装饰器@classmethod 来标识其为类方法，对于类方法，
第一个参数必须是类对象，一般以c1s作为第一个参数。

类方法使用场景
·当方法中需要使用类对象（如访问私有类属性等）时，定义类方法
·类方法一般和类属性配合使用
"""

class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth

xiaoqi = Dog()
result = xiaoqi.get_tooth()
print(f'result = {result}')
