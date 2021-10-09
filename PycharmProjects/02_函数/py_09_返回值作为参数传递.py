# 定义两个函数
# 1.有个返回值
# 2.函数二把返回值作为参数传入

def test1():
    return 50


def test2(num):
    print(num)


test2(test1())