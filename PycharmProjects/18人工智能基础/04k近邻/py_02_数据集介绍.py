# 小规模数据获取

# 加载获取尾花数据集
from sklearn.datasets import load_iris, fetch_20newsgroups

# 小数据集， 该数据集从本地获取
# sklearn.datasets.load_*
# 大数据集， 该数据从网上下载
# sklearn.datasets.fetch_*

# 数据集获取
# 1.1小数据集
iris = load_iris()
# print(iris)  # 数据集

# 1.2大数据集
news = fetch_20newsgroups(data_home=None,subset='train')
# subset：'train'或者'test'，'all'，可选，选择要加载的数据集。
# 训练集的“训练”，测试集的“测试”，两者的“全部”

# print(news)
print("鸢尾花数据集的返回值：\n", iris)
# 返回值是一个继承自字典的Bench
print("鸢尾花的特征值:\n", iris["data"])
print("鸢尾花的目标值：\n", iris.target)
print("鸢尾花特征的名字：\n", iris.feature_names)
print("鸢尾花目标值的名字：\n", iris.target_names)
print("鸢尾花的描述：\n", iris.DESCR)

# load和fetch返回的数据类型datasets.base.Bunch(字典格式)
# data：特征数据数组，是 [n_samples * n_features] 的二维 numpy.ndarray 数组
# target：标签数组，是 n_samples 的一维 numpy.ndarray 数组
# DESCR：数据描述
# feature_names：特征名,新闻数据，手写数字、回归数据集没有
# target_names：标签名