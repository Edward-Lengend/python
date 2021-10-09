"""
for 临时变量 in 序列
    重复执行的代码
    。。。
"""

str1 = "hello world"
for i in str1:
    print(i, end="")

print("")

str2 = "hello world"
for a in str2:
    if a == ' ':  # 遇到空格不打印后面
        break
    print(a, end="")
