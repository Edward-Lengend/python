"""
方法一

1.导入
import 包名.模块名
2.调用功能
包名.模块名.功能()
"""

# import my_package.moudle1
# my_package.moudle1.print_info()

"""
方法二
必须在__init__.py文件中添加__al1__ = []，控制允许导入的模块列表。
然后可以使用 from 包 import *
通过模块名.方法可以调用
"""
from my_package import *
moudle2.print_info()
