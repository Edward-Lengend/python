# {}键值对  用逗号隔开

# 1.创建有数据字典
dict1 = {'name': 'Tom', 'age': '20', 'gender': 'man'}


# # 2.创建无数据字典
# dict2 = {}
# # 或
# dict3 = dict()
# print(type(dict2))
# print(type(dict3))
#
# # 3.字典是不支持下标的
# print(dict1['name'])
#
# # 4.增加数据
# # 在最后增加数据
# dict1['id'] = 2
# print(dict1)
#
# # 5.删除数据
#
# #del
# del dict1['name']  # 按照key删除
# print(dict1)

# 6.修改
# dict1['name'] = 'Jerry'

# # 7.查找
# # key值查找
# print(dict1['name'])
# # 函数查找
# # get
print(dict1.get('name'))
print(dict1.get('names'))  # 不存在返回None
print(dict1.get('names', 'No'))  # 不存在返回No

# keys()
print(dict1.keys())  # 列出字典中所有的key, 返回可迭代对象

# values()
print(dict1.values())  # 列出字典中所有的value, 返回可迭代对象

# items()
print(dict1.items())




