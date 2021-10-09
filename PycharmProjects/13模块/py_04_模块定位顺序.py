"""
当导入一个模块，Python解析器对模块位置的搜索顺序是：
1.当前目录
2.如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。
3.如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/

模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，
PYTHONPATH和由安装过程决定的默认目录。




"""
# 注意
# 1.自己的文件名不要和已有模块名重复，否则导致模块功能无法使用
# import random
# num = random.randint(1, 5)
# print(num)

# 2.使用from模块名import功能的时候，如果功能名字重复，调用到的是最后定义或导入的功能。
from time import sleep


def sleep():
    print('自定义sleep')


sleep(2)
print('hello')