import pandas as pd
import numpy as np


stock_change = np.random.normal(0, 10, (10, 5))
# print(stock_change)

# 增加行列信息
stock_rise = pd.DataFrame(stock_change)  # 该数据为DataFrame类型
# print(stock_rise)

# 查看表格形状
# print(stock_rise.shape)
# 表格一维（行）数
# print(stock_rise.shape[0])
# 表格二维（列）数
# print(stock_rise.shape[1])

# 制作行索引
stock_code = ["股票{}".format(i + 1) for i in range(stock_rise.shape[0])]
# print(stock_code)

# 将表格中的列信息替换
# new_stock =
pd.DataFrame(stock_change, index=stock_code)  # index=表示行索引， columns=表示列索引
#                         ↑只能传ndArray!不能传入DataFrame



# 准备列索引（日期）                           时间跨度                       工作日
date = pd.date_range(start="2021-10-02", periods=stock_rise.shape[1], freq='B')
# print(date)
new_stock = pd.DataFrame(stock_change, index=stock_code, columns=date)
print(new_stock)

print(new_stock.shape)
print(new_stock.index)
print(new_stock.columns)
print(new_stock.values)
print(new_stock.T)

# 看前几行/后几行
print(new_stock.head(2))  # 前两行
print(new_stock.tail(2))  # 后两行

# 重设索引
new_stock.reset_index(drop=True)


# 以某列设置新索引案例
df = pd.DataFrame({"month": [1, 4, 7, 10],
                   'year': [2011, 2012, 2013, 2014],
                   'sale': [55, 40, 84, 31]
                })
print(df)

new_df = df.set_index(keys=['year'])
print(new_df)

# 设置多个列索引
print(df.set_index(keys=["year", "month"]))