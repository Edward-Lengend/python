class A:  # 父类
    def __init__(self):
        self.num = 1

    def print_info(self):
        print(f'num = {self.num}')


class B(A):  #子类
    pass


result = B()
result.print_info()
