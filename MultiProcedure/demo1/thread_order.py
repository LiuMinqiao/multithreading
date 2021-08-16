import threading
import time


def task():
    time.sleep(1)
    # 获取当前线程的线程对象
    thread = threading.current_thread()
    print(thread)

if __name__=="__main__":
    for i in range(6):
        sub_thread = threading.Thread(target=task)
        sub_thread.start()
        # 执行顺序无序，由cpu进行调度
        # 线程依附在进程里面的