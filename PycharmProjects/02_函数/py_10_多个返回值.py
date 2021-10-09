def return_num():
    return 1, 2  # 返回元组


result = return_num()
print(result)


# return 可以直接书写元组、列表、字典
def return_num1():
    # return [100, 200]
    return {'name': 'Tom', 'age': 18}