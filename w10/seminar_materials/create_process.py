import multiprocessing

def cpu_intensive():
    a, b = 1, 1
    for i in range(10**8):
        a, b = a+b, a
    return a


processes = [multiprocessing.Process(target=cpu_intensive) for i in range(3)]
for process in processes:
    process.start()
print('22')
for process in processes:
    process.join()
print('finished')

