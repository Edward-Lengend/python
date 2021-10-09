import pandas as pd
import numpy as np

data = pd.read_csv("stock_day.csv")
data = data.drop(["ma5","ma10","ma20","v_ma5","v_ma10","v_ma20"], axis=1)
# print(data.head())

# 将某一列的值加上一个数
data['open'].add(10)  # 或data['open']+10
# print(data)

# 逻辑运算符号
# 例如筛选data["open"] > 23的日期数据
# print(data["open"] > 23)
# print(data[data["open"] > 23])  # 拿到整行

# &
# print(data[(data['open'] > 24) & (data['open'] < 24.2)])

# query(expr)
#expr:查询字符串
#通过query使得刚才的过程更加方便简单

# print(data.query("open<24 & open>23").head())

# isin(values)
# 例如判断'open'是否为23.53和23.85

# 可以指定值进行一个判断，从而进行筛选操作
print(data[data["open"].isin([23.53, 23.85])])