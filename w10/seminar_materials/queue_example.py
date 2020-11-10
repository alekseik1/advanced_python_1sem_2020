from multiprocessing import Process, Queue


def f(q):
    # FIFO
    q.put([42, None, 'hello'])
    q.put([-1])


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    p.join()
    while not q.empty():
        print(q.get())

