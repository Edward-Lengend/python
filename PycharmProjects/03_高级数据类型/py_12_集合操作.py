s1 = {10, 20}

s1.add(100)  # 追加到任意一个位置
print(s1)

# add不能增加序列
# s1.add([20, 30])  # 追加到任意一个位置
# print(s1)

# 增加序列要使用update
# s1.update([40, 20, 30])
# print(s1)

# 删除
# remove() 指定数据
# s1.remove(10) # 删除不存在的数据会报错

# discard
s1.discard(5000)  # 删除的数据不存在不会报错

# pop
# del_num = s1.pop()
# print("删除了%d" % del_num)  # 随机删除

# 查找数据是否存在
print(10 in s1)  # 存在返回True， 否则False
print(10 not in s1)  # 相反

