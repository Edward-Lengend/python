import os
# 把该文件下的文件全重命名， 前面加上‘python_’

# 1.找到所有文件的名字

# file_list = os.listdir()
# print(file_list)

# 2.获取名字、重命名

# for i in file_list:
#     new_name = 'python_' + i
#     os.rename(i, new_name)

# 3.批量删除前缀
new_file_list = os.listdir()
for i in new_file_list:
    index = i.find('_')
    new_name = i[index + 1:]
    os.rename(i, new_name)


