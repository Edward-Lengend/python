# enumerate(可遍历对象, start=0)
# 注意：start参数用来设置遍历数据的下标的起始值，默认为0。
list1 = []
list1.extend("abcde")
print(list1)

# enumerate返回结果是元组
# 第一个参数是原迭代对象的下标
# 第二个参数是原迭代对象的数据
for i in enumerate(list1):
    print(i)
# 数据不变， 下标从1开始4
for i in enumerate(list1, start=1):
    print(i)