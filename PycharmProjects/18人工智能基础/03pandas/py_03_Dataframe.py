import pandas as pd
import numpy as np

# DataFrame(2-D)
# pd.DataFrame(data=None, index=None, columns=None)
# 参数：

# index：行标签。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。
# columns：列标签。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。
# 通过已有数据创建
#
# 举例一：  只导入data
#
score_1 = pd.DataFrame(np.random.randn(2,3))  # 两行三列，从标准正态分布中返回一个或多个样本值
# print(score_1)


# 举例二：创建学生成绩表
# 生成10名同学，5门功课的数据
score = np.random.randint(40, 100, (10, 5))


# 这样的数据形式很难看到存储的是什么的样的数据，可读性比较差！！
# 问题：如何让数据更有意义的显示？
# 使用Pandas中的数据结构
score_df = pd.DataFrame(score)  # 传入data
# print(f'score_df = {score_df}')

# 构造行索引序列
subjects = ["语文", "数学", "英语", "政治", "体育"]

# 构造列索引序列
stu = ['同学{}'.format(i+1) for i in range(score_df.shape[0])]


data = pd.DataFrame(score, columns=subjects, index=stu)

# print(data)

# print(f'data.shape = {data.shape}') # 查看数组形状

# index
# DataFrame的行索引列表

# print(f'data.index = {data.index}')


# columns
# DataFrame的列索引列表
# print(data.columns)

# 修改行列索引值
stu = ["学生_" + str(i) for i in range(score_df.shape[0])]

# 必须整体全部修改
data.index = stu
# print(data.index)


# 重设索引
# reset_index(drop=False)
# 置新的下标索引
# drop:默认为False，不删除原来索引，如果为True,删除原来的索引值
# 重置索引,drop=False
# data.reset_index()