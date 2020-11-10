from multiprocessing import Process, Pipe
import time


def f(conn):
    pass
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # выводит "[42, None, 'hello']"
    p.join()
