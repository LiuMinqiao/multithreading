import threading
import time
def sing():
    for i in range(2):
        print("sing...")
        time.sleep(1)

def dance():
    for i in range(2):
        print("dancing...")
        time.sleep(1)

def work():
    for i in range(10):
        print("working ...")
        time.sleep(0.2)


if __name__=="__main__":
    # sing_thread = threading.Thread(target=sing)
    # dance_thread = threading.Thread(target=dance)
    #
    #
    # sing_thread.start()
    # dance_thread.start()
    # 设置子线程为守护进程
    # sub_thread = threading.Thread(target=work,daemon=True)
    # or
    sub_thread = threading.Thread(target=work)
    sub_thread.daemon = True
    # sub_thread.setDaemon(True)

    sub_thread.start()
    time.sleep(1)
    print("主线程结束....")