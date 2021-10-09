# readlines()

f = open('test.txt', 'r')

# content = f.readlines()  # 返回一个列表，每个元素为一行内容
#
# print(content)

# readline()
content = f.readline()
print(content, end='')
content = f.readline()
print(content, end='')

