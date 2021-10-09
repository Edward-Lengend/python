"""
 seek(偏移量, 起始位置）
 起始位置：
 0 开头
 1 当前
 2 结尾
"""


f = open("test.txt", 'r')
content = f.read()
print(content)

f.seek(2, 0)
new_content = f.read()
print(new_content)
