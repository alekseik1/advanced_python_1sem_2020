import threading
import time
import random

result = 0

# Примитивы синхронизации
# Mutex

def func1(lock):
    global result
    lock.acquire()
    tmp = result
    result = tmp + 2
    lock.release()

def func1_with(lock):
    global result
    with lock:
        tmp = result
        result = tmp + 2
    # with open('1.txt', 'r') as f:
    #     ...
    # <another_code>


lock = threading.Lock()
threads = [threading.Thread(target=func1_with, args=(lock, )) for i in range(2)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(result)

