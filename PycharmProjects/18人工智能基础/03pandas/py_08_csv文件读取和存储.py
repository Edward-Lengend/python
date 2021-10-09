import numpy as np
import pandas as pd

# read_csv
# pandas.read_csv(filepath_or_buffer, sep =',', usecols )
#
# filepath_or_buffer:文件路径
# sep :分隔符，默认用","隔开
# usecols:指定读取的列名，列表形式

data = pd.read_csv("./data/stock_day.csv", usecols=['open', 'high', 'close'])
# print(data)


# 写文件

# to_csv
# DataFrame.to_csv(path_or_buf=None, sep=', ’, columns=None,
#                           header=True, index=True, mode='w', encoding=None)
#
# path_or_buf :文件路径
# sep :分隔符，默认用","隔开
# columns :选择需要的列索引
# header :boolean or list of string, default True,是否写进列索引值
# index:是否写进行索引  True为要索引
# mode:'w'：重写, 'a' 追加
# 举例：保存读取出来的股票数据
#
# 保存'open'列的数据，然后读取查看结果


# 举例：保存读取出来的股票数据
#
# 保存'open'列的数据，然后读取查看结果
# 选取10行数据保存,便于观察数据
data[:10].to_csv("./data/test_data.csv", columns=['open'])

#
# HDF5
# 2.1 read_hdf与to_hdf
# HDF5文件的读取和存储需要指定一个键，值为要存储的DataFrame
#
# pandas.read_hdf(path_or_buf，key =None，** kwargs)
#
# 从h5文件当中读取数据
#
# path_or_buffer:文件路径
# key:读取的键
# return:Theselected object
# DataFrame.to_hdf(path_or_buf, key, *\kwargs*)
#
# 2.2 案例
# 读取文件
# # day_close = pd.read_hdf("./data/day_close.h5")
# 存储文件
# day_close.to_hdf("./data/test.h5", key="day_close")
# 再次读取的时候, 需要指定键的名字
#
# new_close = pd.read_hdf("./data/test.h5", key="day_close")
# 注意：优先选择使用HDF5文件存储
#
# HDF5在存储的时候支持压缩，使用的方式是blosc，这个是速度最快的也是pandas默认支持的
# 使用压缩可以提磁盘利用率，节省空间
# HDF5还是跨平台的，可以轻松迁移到hadoop 上面