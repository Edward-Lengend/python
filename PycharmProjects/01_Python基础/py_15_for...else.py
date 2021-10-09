str1 = "hello world"
for i in str1:
    print(i, end="")
    if i == " ":
        break
else:
    print("循环正常结束时执行")