#导入进程包
import multiprocessing
import time
import os


def sing(num, name):
    print("唱歌的pid ",os.getpid())
    #获取父进程pid
    print("唱歌的Ppid ",os.getppid())
    for i in range(num):
        print(name)
        print("唱歌...")
        time.sleep(0.5)


def dance(num, name):
    print("跳舞的pid ", os.getpid())
    print("跳舞的ppid ", os.getppid())
    for i in range(num):
        print(name)
        print("跳舞...")
        time.sleep(0.5)


if __name__=='__main__':
    print("主进程pid",os.getpid())
    # sing()
    # dance()
    # 使用进程类创建进程对象
    # target:指定进程执行的函数名
    # args or kargs 传参
    sing_process = multiprocessing.Process(target=sing, args=(3, "小明"))

    dance_process = multiprocessing.Process(target=dance,
                                            kwargs={
                                                "name": "xiaohong",
                                                "num": 3})
    # 启动指定任务
    sing_process.start()
    dance_process.start()
