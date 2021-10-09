"""
导入模块的方式

·import模块名
·from模块名import功能名
·from模块名import*
·import 模块名as别名
·from模块名import功能名as别名
"""

# 方法一
# import math
# print(math.sqrt(0.16))

"""
方法二
from math import sqrt  # (不需要写“模块名.功能”)
print(sqrt(9))
"""

# 方法三：
from math import *  # (不需要写“模块名.功能”)
print(sqrt(9))

