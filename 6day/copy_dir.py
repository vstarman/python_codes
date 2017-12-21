import os
from multiprocessing import Pool,Manager

def copy_file_task(file_name,old_folder_name,new_folder_name, queue): 
	"""完成copy一个文件功能"""     
	fr = open((old_folder_name+"/"+file_name),"rb")
	fw = open((new_folder_name+"/"+file_name),"wb")

	content = fr.read()
	fw.write(content)

	fr.close()
	fw.close()

	queue.put(file_name)

def main():
    
	# 取要copy的文件夹名字     
	old_folder_name = input("请输入要copy的文件夹名:")

	# 创建一个文件夹
	new_folder_name = old_folder_name+"-[复件]"
	os.mkdir(new_folder_name)

	# 获取老文件夹所有的文件名字
	old_folder_list = os.listdir(old_folder_name)

	# 使用多进程方式copy源文件所有文件到nw文件夹
	pool = Pool(5)
	queue = Manager().Queue()

	for file_name in old_folder_list:
		pool.apply_async(copy_file_task, args=(file_name,old_folder_name,new_folder_name,queue))

	num = 0
	all_num = len(old_folder_list)
	while num < all_num:
		queue.get()
		num += 1
		copy_rate = num/all_num
		print("\rcopy的进度为:%.2f%%"%(copy_rate*100),end="")
	print("\n已完成copy.....")
	pool.close()
	pool.join()


if __name__ == '__main__':
	main()


