# Pandas中一共有三种数据结构，分别为：Series、DataFrame和MultiIndex（老版本中叫Panel ）。
#
# 其中Series是一维数据结构，DataFrame是二维的表格型数据结构，MultiIndex是三维的数据结构。
#
# 1.Series
# Series是一个类似于一维数组的数据结构，它能够保存任何类型的数据，
# 比如整数、字符串、浮点数等，主要由一组数据和与之相关的索引两部分构成。

# 导入pandas
import pandas as pd
import numpy as np

# pd.Series(data=None, index=None, dtype=None)
# 参数：
# data：传入的数据，可以是ndarray、list等
# index：索引，必须是唯一的，且与数据的长度相等。
#        如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。
# dtype：数据的类型

series_1 = pd.Series(np.arange(1, 10))
print(f'series_1 = {series_1}')  # 索引为0~8， 数字为1~9

# 指定索引
series_2 = pd.Series([6.7,5.6,3,10,2], index=np.arange(1, 6))
# print(f'series_2 = {series_2}')

# 通过字典数据创建          index： value
color_count = pd.Series({'red':100, 'blue':200, 'green': 500, 'yellow':1000})
# print(color_count)

# Series的属性
# 为了更方便地操作Series对象中的索引和数据，Series中提供了两个属性index和values

# print(color_count.index)  # 查看index
# Index(['blue', 'green', 'red', 'yellow'], dtype='object')

# values
# color_count.values  # 可以查看values

# 使用索引来获取数据：
print(color_count[2])