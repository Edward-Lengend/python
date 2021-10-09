
# 正太分布图像
# 正态分布创建方式
# np.random.randn(d0, d1, …, dn)
# 功能：从标准正态分布中返回一个或多个样本值
# np.random.normal(loc=0.0, scale=1.0, size=None)
# loc：float
# 此概率分布的均值（对应着整个分布的中心centre）

# scale：float
# ​ 此概率分布的标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）

# size：int or tuple of ints
# ​ 输出的shape，默认为None，只输出一个值

# np.random.standard_normal(size=None)
# 返回指定形状的标准正态分布的数组。

import matplotlib.pyplot as plt
import numpy as np

#                   均值          方差            个数
x = np.random.normal(loc=175, scale=1.0, size=100000000)

print(x)

plt.figure(figsize=(20, 20), dpi=100)

plt.hist(x, bins=500)  # x代表要使用的数据， bins代表要划分的区间数
plt.show()

