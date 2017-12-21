import os
from multiprocessing import Pool

def copy_file_task():
    pass

def main():

# 获取要copy的文件夹的名字
old_folder_name = input("Plesae input file name you want to copy:")

# 创建新文件夹
new_folder_name = old_folder_name + "-复件"
os.mkdir(new_folder_name)

# 获取old文件文件列表
file_list = os.listdir(old_folder_name)
#print(file_list)


# 使用多线程方式copy 拷贝文件到新文件夹
poll = Pool(5)

pool.apply_async()











