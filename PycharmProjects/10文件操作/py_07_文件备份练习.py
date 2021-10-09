"""
需求：用户输入当前目录下任意文件名
程序完成对该文件的备份功能（备份文件名为xx[备份]后缀
例如：test[备份].txt）。
"""

# 用户输入目标文件
old_name = input('请输入您要备份的文件名：')

# 规划备份文件的名字
index = old_name.rfind('.')

# 后缀
if index > 0 and index != len(old_name) - 1:
    postfix = old_name[index:]
else:
    print('文件名不符合规范')
    exit()

# 新名字 = 原名+【备份】+ 后缀
new_name = old_name[0:index:1] + '[备份]' + postfix

# 文件大小不确定， 需要循环读取， 否则文件过大容易卡死

old_f = open(old_name, 'rb')
new_f = open(new_name, 'wb')

while True:
    content = old_f.read(1024)  # 一次性读取1024个字节
    new_f.write(content)
    if len(content) == 0:  # 文件到末尾
        break

new_f.close()
old_f.close()




f.close()

