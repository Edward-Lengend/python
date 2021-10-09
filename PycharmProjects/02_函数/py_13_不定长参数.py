# 用于不确定调用的时候会传递多少个参数的场景
# 此时可以用包裹（packing）位置参数，或者包裹关键字参数，来进行参数传递

# 1.包裹位置传递，根据参数传进位置合并成一个元组
def user_info(*args):
    #  args代表arguments
    print(args)


user_info('Tom', 19)
user_info('Tom', 19, 'Man')


# 2.包裹关键字传递
def user_info1(**kwargs):
    print(kwargs)  # kwargs -> key words arguments


user_info1(name='Tom')  # name是形参名字
user_info1(name='Tom', age=18, gender='M')