f = open('test.txt', 'r')
# content = f.read()
# # read不写参数表示读取整个文件
# print(content)

content1 = f.read(10)  # 读取10个字节
print(content1)

f.close()