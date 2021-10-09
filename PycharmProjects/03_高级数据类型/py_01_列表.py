name_list = ["zhangSan", "LiSi", "WangWu"]

# 1.取值和索引
print(name_list[2])

# 知道数据的内容，想确定数据在列表中的位置
print(name_list.index("LiSi"))  # 返回下标
# 使用index方法需要注意，如果数据不在索引中，程序会报错
# print(name_list.index("haha"))

# 2.修改
name_list[0] = "张三"
print(name_list[0])
# name_list.reverse()



# 3.增加
# 3种方法 insert append extend
name_list.append("王小二")  # 在最后追加

name_list.insert(3, "傻逼")  # 在列表指定位置插入数据

temp_list = ["悟空", "八戒", "沙僧"]
name_list.extend(temp_list)
name_list.extend('haha') # 追加字符串， 会逐一追加到列表
name_list.extend(["hello", "world"])

# # 4.删除数据
# # remove
# name_list.remove("WangWu")  # 删除指定数据
#
# # pop
# name_list.pop()  # 把最后一个数据删除
# name_list.pop(3)  # 也可以指定索引
#
# # clear
# # name_list.clear()  # 清空列表
#
# # del
# del name_list[2]  # del是把这个变量从内存中删除，后续不能再使用这个变量
# # 删除列表数据尽量使用列表提供的接口， 不要使用del
#
# # 5.len长度
# list_len = len(name_list)
# print("list_len = %d" % list_len)
#
# # 6.count 统计列表中某一个数据出现的次数
# count = name_list.count("张三")
# print("张三出现的次数为%d" % count)
#
# # 7.remove只按值删除出现的第一个数据
# name_list.append("张三")
# name_list.remove("张三")
#
# # 8. 判断数据是否存在于列表中
# print('LiSi' in name_list)  # 存在返回True, 不存在返回False
# print('LiSi' not in name_list)  # 不存在返回True, 存在返回False

# 打印测试
print(name_list)
