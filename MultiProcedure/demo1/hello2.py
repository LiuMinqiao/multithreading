import threading
import time
def sing(num, name):
    print(name,": 唱歌")
    for i in range(num):
        print("sing...")
        time.sleep(1)

def dance(num):
    for i in range(num):
        print("dancing...")
        time.sleep(1)


if __name__=="__main__":
    sing_thread = threading.Thread(target=sing, args=(3, "xiaoming"))
    dance_thread = threading.Thread(target=dance, args=(3,))

    dance_thread.start()
    sing_thread.start()