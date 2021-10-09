import time
from student import *


class StudentManager(object):
    def __init__(self):
        # 存储学员数据
        self.student_list = []

    # 程序入口
    def run(self):
        # 加载文件中的学员数据
        self.load_student()

        while True:
            # 显示功能菜单
            self.show_menu()
            # 用户输入系统功能
            print('')
            try:
                menu_num = int(input('请输入您需要的功能:'))
            except ValueError:
                print('请输入数字！')
                time.sleep(1)
                continue

            # 执行功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统
                break
            else:
                print('没有该功能')
                time.sleep(2)

    # 二.系统功能函数
    # 2.1显示功能菜单
    @staticmethod
    def show_menu():
        print('请选择如下功能：')
        print('1.添加学员')
        print('2.删除学员')
        print('3.修改学员信息')
        print('4.查询学员信息')
        print('5.显示所有学员信息')
        print('6.保存学员信息')
        print('7.退出')

    # 2.2添加学员
    def add_student(self):
        # 用户输入姓名、性别、手机号
        name = input('请输入学员姓名')
        gender = input('请输入学员性别')
        tel = input('请输入学员手机号')

        # 创建学员对象
        new_student = Student(name, gender, tel)

        # 将该对象添加到学员列表
        self.student_list.append(new_student)
        print(self.student_list)
        print(new_student)

    # 2.3删除学员
    def del_student(self):
        del_name = input('请输入您要删除的学员姓名')

        # 目标学员姓名存在则删除， 否则提示不存在
        for i in self.student_list:
            if del_name == i.name:
                self.student_list.remove(i)
                break
        else:
            print('该学员不存在！')

        print(self.student_list)

    # 2.4修改学员信息
    def modify_student(self):
        modify_name = input('请输入您要修改的学员的姓名：')
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input('请输入新的学员姓名：')
                i.gender = input('请输入新的学员性别：')
                i.tel = input('请输入新的学员电话：')
                print('新的学员信息为：')
                print(f'姓名： {i.name}  性别：{i.gender}, 电话：{i.tel}')
                input()
                break
        else:
            print('没有此学员！')
            input()



    # 2.5查询学员信息
    def search_student(self):
        search_name = input('请输入您要查询的学员姓名：')
        for i in self.student_list:
            if search_name == i.name:
                print(f'姓名： {i.name}  性别：{i.gender}, 电话：{i.tel}')
                input()
                break
        else:
            print('该学员不存在！')
            input()

    # 2.6显示所有学员信息
    def show_student(self):
        print('姓名\t性别\t手机号')
        for i in self.student_list:
            print(i)
            input()

    # 2.7保存学员信息
    def save_student(self):
        # 1.打开文件
        f = open('student.data', 'w')

        # 2.文件写入学员数据
        # 注意1：文件写入的数据不能是学员对象的内存地址，需要把学员数据转换成列表字典数据再做存储
        # 注意2：文件内数据要求为字符串类型，故需要先转换数据类型为字符串才能文件写入数据
        new_list = [i.__dict__ for i in self.student_list]
        f.write(str(new_list))

        # 3.关闭文件
        f.close()

    # 2.8加载所有学员信息
    def load_student(self):
        # 打开数据
        try:
            f = open('student.data', 'r')
        except FileNotFoundError:
            return

        # 读取数据， 文件中读取出来的数据是字符串， 需要还原列表类型
        # [{}]需要还原成[学员对象]
        data = f.read()
        new_val = eval(data)  # 还原
        self.student_list = [Student(i['name'], i['gender'],
                                     i['tel']) for i in new_val]

        # 关闭文件
        f.close()
