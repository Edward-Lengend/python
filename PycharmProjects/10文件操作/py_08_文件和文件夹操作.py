"""
1.导入模块OS
2.使用模块功能
"""
import os

f1 = open('1.txt', 'w')
f1.close()
f2 = open('2.txt', 'w')
f2.close()

# 1. rename()  可以重命名文件或文件夹
# rename(src, dst)
os.rename('1.txt', '10.txt')

# 2.remove()删除文件
os.remove('10.txt')

# 3.创建文件夹 mkdir
# os.mkdir('aa')

# 4.删除文件夹 rmdir
# os.rmdir('aa')

# 5. 获取当前路径 getcwd
print(os.getcwd())

# 6.切换目录
# 在aa文件夹下创建bb文件夹
# os.chdir('aa')  # 切换目录
# os.mkdir('bb')
# os.chdir('..')
# os.mkdir('haha')

# 7.获取某文件夹下所有文件名 listdir
print(os.listdir('.'))