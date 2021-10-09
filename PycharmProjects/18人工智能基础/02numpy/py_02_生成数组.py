import numpy as np

#  生成0和1的数组
# np.ones(shape, dtype)
# np.ones_like(a, dtype)
# np.zeros(shape, dtype)
# np.zeros_like(a, dtype)

#　１数组
ones = np.ones([4, 8], dtype=np.int8)
# print(ones)

# 0数组
zeros = np.zeros_like(ones)    # 按照ones数组形状创建0数组
# print(zeros)

# 从现有数组生成
array_a = np.array([[1, 2, 3], [4, 5, 6]])
array_a1 = np.array(array_a)
# print(array_a)
# print(array_a1)
array_a[0, 1] = 1000
# print(array_a[0, 1])
# print(array_a1[0, 1])         # np.array是深拷贝

array_b1 = np.asarray(array_a)
array_a[0, 2] = 1000
# print(array_b1[0, 2])         # np.asarray是浅拷贝

# 生成固定范围数组

# np.linspace (start, stop, num, endpoint)
# 创建等差数组 — 指定数量
# 参数:
# start:序列的起始值
# stop:序列的终止值
# num:要生成的等间隔样例数量，默认为50
# endpoint:序列中是否包含stop值，默认为ture
A = np.linspace(0, 50, 10, )  # 0到50生成十个
# print(A)

# np.arange(start,stop, step, dtype)
# 创建等差数组 — 指定步长
# 参数
# step:步长,默认值为1
c = np.arange(10, 20, 2)
# print(f'c = {c}')
c1 = np.arange(10)
print(f'c1 = {c1}')  # 0 1 2 3 4 5 6 7 8 9

# np.logspace(start,stop, num)
# 创建等比数列
# # 生成10^x
d = np.logspace(0, 2, 3)  # 十的零次到2次生成三个数
# print(d)


# 生成随机数组

# 均匀分布
# print(np.random.rand(2, 3))  # 两行三列， 返回[0.0，1.0)内的一组均匀分布的数。


# np.random.uniform(low=0.0, high=1.0, size=None)
# 功能：从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high.
# 参数介绍:
# low: 采样下界，float类型，默认值为0；
# high: 采样上界，float类型，默认值为1；
# size: 输出样本数目，为int或元组(tuple)类型，例如，size=(m,n,k), 则输出mnk个样本，缺省时输出1个值。
# 返回值：ndarray类型，其形状和参数size中描述一致。
f = np.random.uniform(low=-1, high=10,size=(4, 6))
# print(f)


# np.random.randint(low, high=None, size=None, dtype='l')
# 从一个均匀分布中随机采样，生成一个整数或N维整数数组，
# 取数范围：若high不为None时，取[low,high)之间随机整数，否则取值[0,low)之间随机整数。
g = np.random.randint(0, 5, (3, 5))
# print(f'g = {g}')


