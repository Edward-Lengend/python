import matplotlib.pyplot as plt
import numpy as np

#
stock_change = np.random.uniform(0, 1, (8, 10))
#                前两行   前三列
# print(stock_change[0:2, 0:3])

# 形状修改
# ndarray.reshape(shape, order)
# 返回一个具有相同数据域，但shape不一样的视图
# 行、列不进行互换
# 在转换形状的时候，一定要注意数组的元素匹配
stock_change.reshape([10, 8])  # 改为5行4列， 生成新的ndarray
stock_change.reshape([-1,10])  # 数组的形状被修改为: (2, 10), -1: 表示通过待计算，要能整除
stock_change.resize([8, 10])  # 在原来ndarray的基础上修改
print(stock_change.T)  # 转置
