def return_result(num):
    if num == 1:
        return 1
    else:
        return num + return_result(num - 1)


num = 10
print(f'1 + 2 + ... + {num} = {return_result(num)}')
