row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %-2d" % (col, row, col * row), end="  ")
        col+= 1
    print("")
    row += 1


