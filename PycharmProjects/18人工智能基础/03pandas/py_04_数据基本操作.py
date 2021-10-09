import numpy as np
import pandas as pd
import pprint  # 使用pprint.pprint()代替print，可以使数据更美观
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)




data = pd.read_csv("stock_day.csv")  # 从文件中读取数据
# print(stock_data.head())  # 默认查看前5行

# 删除一些列，让数据更简单些，再去做后面的操作
data = data.drop(["ma5","ma10","ma20","v_ma5","v_ma10","v_ma20"], axis=1)  # axis -> 0行1列

# print(data.head())

# --------索引操作----------
# 直接使用行列索引(先列后行)
# 获取'2018-02-27'这天的'close'的结果

# 直接使用行列索引名字的方式（先列后行）先列后行会报错
# print(data['open']['2018-02-27'])


# 不支持的操作
# 错误
# data['2018-02-27']['open']
# 错误
# data[:1, :2]


# 结合loc或者iloc使用索引
#获取从'2018-02-27':'2018-02-22'，'open'的结果

# 使用loc:只能指定行列索引的名字
# print(data.loc['2018-02-27':'2018-02-22', 'open'])  # 查看27到22的open数据

# 使用iloc可以指定读取的行列
# print(data.iloc[:3, :5])  # 前三行，前五列



# ---------组合索引----------
# 获取行第1天到第4天，['open', 'close', 'high', 'low']这个四个指标的结果

# print(data.loc[data.index[0: 4], ['open', 'close', 'high', 'low']])
# 或
# print(data.iloc[0:4, data.columns.get_indexer(['open', 'close', 'high', 'low'])])


# --------给某一列赋值-----------
data['close'] = 1  # 或data.close = 1
# pprint.pprint(data)



# ---------DataFrame排序------------
# 使用df.sort_values(by=, ascending=)
# 单个键或者多个键进行排序,
# 参数：
# by：指定排序参考的键
# ascending:默认升序
# ascending=False:降序
# ascending=True:升序
data = data.sort_values(by="high", ascending=True).head()
# pprint.pprint(data)
# 按照多个键进行排序
data.sort_values(by=['open', 'high'])  # 先按照open排序，再按照high

# 将索引排序
# 这个股票的日期索引原来是从大到小，现在重新排序，从小到大

data = data.sort_index()
# print(data)

# series排序时，只有一列，不需要参数
#
series_1 = data['p_change'].sort_values(ascending=True).head()
print(series_1)