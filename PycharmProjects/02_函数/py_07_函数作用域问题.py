a = 100
# a 是一个全局变量
def test1():
    print(f'a = {a}')


test1()

def test2():
    a = 200  # 函数内部重新定义的a， 作用域为test2， 与全局变量a无关


print(f'a = {a}')  # a 的值并没有改变


# 如何通过函数修改全局变量a？

def test3():
    global a  # 声明a是全局变量的a
    a = 500


test3()
print(f'a = {a}')  # 成功修改为500