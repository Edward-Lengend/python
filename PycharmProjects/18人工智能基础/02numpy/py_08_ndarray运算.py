import numpy as np
stock_change = np.random.normal(0, 1, (8, 10))
stock_c = stock_change[0:5, 0:5]
# print(stock_c)
# print(stock_c > 1)
# stock_c[stock_c > 1] = 2  # 将所有大于1的值改为2
# print(stock_c)

# 通用判断函数
stock_d = stock_change[0:2, 0:5]
print(stock_d)
# all  全部满足返回True
# print(np.all(stock_d > -2)) # 第一行，0到4列是否都大于某值

# any  满足一个返回True
# print(np.any(stock_d > 1.7))

# 三元运算符
# np.where              大于0返回1， 小于0返回-1
# print(np.where(stock_d > 0, 1, -1))

# logical_and                            满足赋值为1， 否则为-1
# print(np.where(np.logical_and(stock_d > -0.5, stock_d < 0.5), 1, -1))

# logical_or
# print(np.where(np.logical_or(stock_d < -0.5, stock_d > 0.5), 1, -1))



# 统计指标
# 在数据挖掘/机器学习领域，统计指标的值也是我们分析问题的一种方式。常用的指标如下：
#
# min(a, axis)
# Return the minimum of an array or minimum along an axis.
# max(a, axis)
# Return the maximum of an array or maximum along an axis.
# median(a, axis)
# Compute the median along the specified axis.
# mean(a, axis, dtype)
# Compute the arithmetic mean along the specified axis.
# std(a, axis, dtype)
# Compute the standard deviation along the specified axis.
# var(a, axis, dtype)
# Compute the variance along the specified axis.

# ---进行统计的时候，axis 轴的取值并不一定------
# Numpy中不同的API轴的值都不一样，在这里，axis 0代表列, axis 1代表行

print(stock_change.max())
print(stock_change.max(axis=0))  # 列最大
print(stock_change.max(axis=1))  # 行最大