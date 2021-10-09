str1 = "hello world, I am Edward. I love this world and python and all you guys"

# 替换
# replace（旧子串,新子串,替换次数）
str1.replace('python', 'Python')  # 次数不写表示全部替换
# replace 不会更改原字符串，会返回一个列表
print(str1)

new_str = str1.replace('python', "111111")
print(new_str)
# 字符串是不可变类型数据

# 2.split 字符串分割   返回列表
# split(分割字符， 分割次数)
list1 = str1.split("and", 1)
print(list1)

# 3.join 合并列表中的小字符串为一个大字符串
list2 = ['aa', 'bb', 'cc']
# 字符或子串.join(多字符串组成的序列)
# 需求： 将list2变成aa...bb...cc
list3 = '...'.join(list2)
print(list3)