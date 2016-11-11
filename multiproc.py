from multiprocessing import Process
import os
import time

k = 10000000

def loop_print(n):
    for i in range(0, n):
        i += 1
        
multi_start = time.time()
for i in range(0, 4):
    p = Process(target=loop_print, args=(k,))
    p.start()
multi_end = time.time()
multi_elapsed = multi_end - multi_start

single_start = time.time()
for i in range(0, 4):
    loop_print(k)
single_end = time.time()
single_elapsed = single_end - single_start

print("Multi time: {} seconds".format(multi_elapsed))
print("Single time: {} seconds".format(single_elapsed))
