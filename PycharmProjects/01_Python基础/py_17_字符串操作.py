str1 = "hello world, i am Edward. I love this world"

#字符串查找
# find  index

# find(子串, 开始下标, 结束下标)
# 找到返回下标
# 未找到返回-1

# index和find用法一样,但index找不到子串会报错

print(str1.find("world"))  # 找到返回下标 下标可以省略
print(str1.find("world", 11, 43))

# count
print(str1.count("world"))  # 子串出现的次数

# rfind 从右侧查找