# range(start, end, step)

# 1 2 3 4 5 6 7 8 9 不包括end
for i in range(1, 10, 1):
    print(i, end="")
print()

# 1 3 5 7 9
for i in range(1, 10, 2):
    print(i, end="")
print()

# 0 1 2 3 4 5 6 7 8 9
for i in range(10):  # 可以省略start，默认从0开始，步长为1
    print(i, end="")
print()
