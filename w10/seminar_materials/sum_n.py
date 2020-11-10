import threading
import multiprocessing
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from collections import defaultdict
from queue import Queue

arr = []
lock = threading.Lock()


def sum_a(my_arr):
    res = sum([i**1 - i**3/3 + i**5/5 for i in my_arr]) # <---
    with lock:
        global arr
        arr.append(res)


def split_array(arr, pieces_number):
    """
    >>> split_array([1, 2, 3, 4], 2)
    >>> [1, 2], [3, 4]
    """
    step = len(arr) // pieces_number
    i = 0
    while i < pieces_number-1:
        yield arr[step*i:step*(i+1)]
        i += 1
    yield arr[step*i:]


def one_run(l, th):
    array = [10]*l
    div = l // th
    threads = []
    for subarray in split_array(array, th):
        threads.append(threading.Thread(target=sum_a, args=(subarray, )))
        # threads.append(multiprocessing.Process(target=sum_a, args=(subarray, )))
        threads[-1].start()
    result = 0
    for thread in threads:
        thread.join(timeout=5)
    return sum(arr)


if __name__ == "__main__":
    LEN = 10**6
    x_data = [1, 2, 4, 8, 10]
    y_data = []
    for thread in x_data:
        tmp_data = []
        for sample in range(3):
            start = datetime.now()
            print(one_run(LEN, thread))
            tmp_data.append((datetime.now() - start).microseconds)
            arr.clear()
        y_data.append(sum(tmp_data)/len(tmp_data))
    plt.plot(x_data, y_data)
    plt.grid()
    plt.ylabel('Время выполнения, [мс]')
    plt.xlabel('Число потоков')
    plt.show()
