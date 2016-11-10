from multiprocessing import Process
import os

def cpu_eat():
    n = 0
    
    while True:
        n += 1

for i in range(0, 4):
    p = Process(target=cpu_eat)
    p.start()
