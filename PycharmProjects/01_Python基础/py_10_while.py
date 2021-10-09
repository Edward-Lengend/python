"""
i = 0
sum = 0
while i <= 100:
    sum += i
    i += 1
print("0 + 1 + 2 + 3 + .. + 100 = %d" % sum)
"""


# 0~100 偶数求和
i = 0
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i = i + 1
print("0~100的偶数和为%d" % sum)