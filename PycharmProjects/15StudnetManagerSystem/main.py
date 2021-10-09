# 1.导入管理系统模块
from manager import *

# 2.启动管理系统
# 保证是当前文件运行才启动管理系统
if __name__ == '__main__':
    student_manager = StudentManager()
    student_manager.run()
    print('欢迎下次使用！')