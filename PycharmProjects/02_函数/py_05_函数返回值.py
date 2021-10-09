def sum_2_num(num1, num2):
    """对两个数字的求和"""

    result = num1 + num2
    return result


sum_result = sum_2_num(2, 10)
print("计算结果：%d" % sum_result)


def print_line(char, times, turn):
    i = 0
    while i < turn:
        print(char * times)
        i += 1


print_line("_", 10, 5)