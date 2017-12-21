import os
import multiprocessing import Pool

def copy_file_task(file_name,old_folder_name,new_folder_name): 
    """完成copy一个文件功能"""     
    fr = open((old_folder_name+"/"+file_name),"rb")
	fw = open((new_folder_name+"/"+file_name),"wb")
    
    content = fr.read(file_name)
    fw.write(content)

    fr.close()
    fw.close()


def main():
    
    # 取要copy的文件夹名字     
    old_folder_name = input("请输入要copy的文件夹名:")

	# 创建一个文件夹
	new_folder_name = old_folder_name+"-[复件]"
	os.mkdir(new_folder_name)

	# 获取老文件夹所有的文件名字
	old_foldir_list = os.listdir(old_folder_name)

	# 使用多进程方式copy源文件所有文件到nw文件夹
	pool = Pool(5)

	for file_name in old_foldir_list:
		pool.apply_async(copy_file_task, args=(file_name,old_folder_name,new_folder_name))

	pool.join()


if __name__ == '__main__':
	main()


