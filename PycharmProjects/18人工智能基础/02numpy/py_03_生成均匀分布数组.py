import matplotlib.pyplot as plt
import numpy as np
# 均匀分布图像
x1 = np.random.uniform(-1, 1, 100000000)  # 生成一亿个数
import matplotlib.pyplot as plt

# 创建画布
plt.figure(figsize=(10, 10), dpi=100)

# 绘制直方图
plt.hist(x=x1, bins=500)  # x代表要使用的数据， bins代表要划分的区间数
plt.show()




