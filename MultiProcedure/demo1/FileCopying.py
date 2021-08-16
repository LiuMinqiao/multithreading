import os
import multiprocessing
def copy_file(file_name, source_dir, dest_dir):
    # 路径拼接
    source_path = source_dir+"/"+file_name

    dest_path = dest_dir+"/"+file_name

    with open(source_path, "rb") as source_file:
        with open(dest_path, "wb") as dest_file:
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break




if __name__=="__main__":
    source_dir = "D:\spark-3.1.1-bin-hadoop2.7\jars"
    dest_dir = "./copyFiler"

    try:
        os.mkdir(dest_dir)
    except:
        print("目标文件夹已经存在！！")
    file_list = os.listdir(source_dir)
    for file_name in file_list:
        sub_process = multiprocessing.Process(target=copy_file,
                                              args=(file_name, source_dir, dest_dir))
        sub_process.start()