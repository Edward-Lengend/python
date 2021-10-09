"""
try：
    可能发生错误的代码
except：
    如果出现异常执行的代码

"""
try:
    f = open('test.txt', 'r')
except:
    f = open('test.txt', 'w')