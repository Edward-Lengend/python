import my_moudle2
from my_moudle2 import *  # 由于有all列表控制，只会导入all列表中的内容

testA()  # 可以调用
# testB()  # 不可以调用  testB没有添加到all列表， 只有all列表里面的功能才能导入
