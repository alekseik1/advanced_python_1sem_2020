import threading
import time
import random


def func1(a, b):
    time.sleep(random.randint(a, b))


threads = [threading.Thread(target=func1, args=(1, 5)) for i in range(4)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print('Finished')

