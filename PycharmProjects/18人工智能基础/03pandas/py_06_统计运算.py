import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)


data = pd.read_csv("stock_day.csv")  # 从文件中读取数据
data = data.drop(["ma5","ma10","ma20","v_ma5","v_ma10","v_ma20", "turnover", "p_change"], axis=1)
data = data.head(20)


# print(data.describe())  # 统计

# 统计函数
# 求和
# print(data.sum(axis=0))
# print(data.sum(axis=1))


df = pd.DataFrame({'COL1': [1, 2, 3, 4],
                   'COL2': [5, 6, 6, 7]})
# 中位数
# print(df.median())

# 获取每列最大/小值的索引
# print(data.idxmax())
# print(data.idxmin())



# 累计统计函数
#   函数	            作用
# cumsum	计算前1/2/3/…/n个数的和
# cummax	计算前1/2/3/…/n个数的最大值
# cummin	计算前1/2/3/…/n个数的最小值
# cumprod	计算前1/2/3/…/n个数的积
data = data.sort_index()
# print(data.head())
# 对price_change进行累计求和
# 排序之后，进行累计求和

stock_rise = data['price_change']
# print(stock_rise.cumsum())

# 做出图像
stock_rise.cumsum().plot()
# plt.show()

# 自定义函数
# apply(func, axis=0)
# func:自定义函数
# axis=0:默认是列，axis=1为行进行运算
# 定义一个对列，最大值-最小值的函数
print(data[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=0))
