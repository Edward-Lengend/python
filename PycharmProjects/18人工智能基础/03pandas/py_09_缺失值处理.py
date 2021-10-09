import numpy as np
import pandas as pd

# 如何处理NaN
# 获取缺失值的标记方式(NaN或者其他标记方式)
#
# 如果缺失值的标记方式是NaN
#
# 判断数据中是否包含NaN：
#
# pd.isnull(df),
# pd.notnull(df)
# 存在缺失值nan:
#
# 1、删除存在缺失值的:dropna(axis='rows')
#
# 注：不会修改原数据，需要接受返回值
# 2、替换缺失值:fillna(value, inplace=True)
#
# value:替换成的值
# inplace:True:会修改原数据，False:不替换修改原数据，生成新的对象
# 如果缺失值没有使用NaN标记，比如使用"？"
#
# 先替换‘?’为np.nan，然后继续处理

movie = pd.read_csv("./data/IMDB-Movie-Data.csv")
print(movie)