"""
需求：进入系统显示系统功能界面，功能如下：
1、添加学员
2、删除学员
3、修改学员信息
4、查询学员信息
5、显示所有学员信息
6、退出系统
"""
import os

info = []


def show_menu():
    print("1、添加学员")
    print("2、删除学员")
    print("3、修改学员信息")
    print("4、查询学员信息")
    print("5、显示所有学员信息")
    print("6、退出系统")
    print('-' * 15)


def add_info():
    """
    添加学员
    :return:
    """
    new_name = input('请输入姓名')
    # 姓名存在则return
    global info
    for i in info:
        if new_name == i['name']:
            print('姓名重复')
            input()
            return
    new_id = int(input("请输入学号"))
    new_phone = input("请输入手机号")
    new_dict = {'name': new_name, 'id': new_id, 'phone': new_phone}
    info.append(new_dict)
    print('添加成功')
    print(info)
    input()


def del_info():
    """删除学员"""
    del_name = input('输入要删除的学员姓名')
    global info
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:  # 循环正常结束才会执行
        print('没有此学员')
        input()
    print(info)
    print('删除成功')
    input()


def modify_info():
    modify_name = input('输入要修改的学员姓名')
    global info
    for i in info:
        if modify_name == i['name']:
            i['id'] = int(input('请输入新的学号'))
            i['phone'] = input('请输入新的手机号')
            break
    else:  # 循环正常结束才会执行
        print('没有此学员')
    print(info)
    input()


def search_info():
    search_name = input('请输入您要查找的学员姓名')
    global info
    for i in info:
        if search_name == i['name']:
            print("该学员信息如下")
            print(f"学员姓名：{i['name']}  学号：{i['id']}  电话： {i['phone']}")
            input()
            break
    else:
        print('没有这个学员')
        input()


def print_all():
    global info
    for i in info:
        print("所有学员信息如下")
        print("学号\t姓名\t手机")
        print(f"{i['name']}\t{i['id']}\t{i['phone']}")
        input()


# 系统功能循环使用
while True:
    # 1.显示功能界面
    show_menu()

    # 用户输入
    user_choose = int(input('请输入您要使用的功能序号:\n'))

    if user_choose == 1:
        add_info()
    elif user_choose == 2:
        del_info()
    elif user_choose == 3:
        modify_info()
    elif user_choose == 4:
        search_info()
    elif user_choose == 5:
        print_all()
    elif user_choose == 6:
        flag = input('是否要退出系统？ y/n')
        if flag == 'y':
            break
    else:
        print("没有该功能！")
        continue

print("欢迎下次使用！")
