from sqlitetest import SQLiteTest
from multiprocessing import Process
from time import time
from random import randint

import threading
import sqlite3
import sys
import os

if __name__ == "__main__":
    MAX_ELEMS = 1000
    lock = threading.Lock()
    test = SQLiteTest('sqlite-test.db', lock)
    cursor = test.cursor
    
    # Create test table
    try:
        cursor.execute('CREATE TABLE test('
                       'id integer PRIMARY KEY,'
                       'texto text,'
                       'id2 integer)') # remember, 255 chars for MySQL
        print('CREATE TABLE')

        # Create index for the test table
        cursor.execute('CREATE INDEX id ON test (id)')
        print('CREATE INDEX')

        # Fill table with 1000000 elements
        print("Filling...")
        test.insert(0, MAX_ELEMS)

    except sqlite3.Error as e:
        pass

    print("Success!\n")
    
    try:
        # elements = [10, 1000, 100000, 300000]
        elements = [10, 100, 1000, 3000]
        process = [1, 10, 50]
        j = MAX_ELEMS # Hardcoded, yes!
        
        # Escenario 1
        print("\nSCENARIO 1:")
        
        for e in elements:
            for proc in process:
                start = time()
                what = e/proc
                
                print('ins = %d \t procs = %d \t per = %d'
                      % (e, proc, what))
                
                for i in range(0, proc):
                    min_limit = int(j + what * i)
                    max_limit = int(j + what * (i + 1))
                    
                    p = Process(target=test.insert,
                                args=(min_limit, max_limit))
                    p.start()
                    p.join()
                
                end = time()
                elapsed = end - start
                j += e
                print(j)
                print("Time elapsed: %.5f\n" % elapsed)

        # Escenario 2

        for e in elements:
            for proc in process:
                start = time()
                what = e/proc
                
                print('ins = %d \t procs = %d \t per = %d'
                      % (e, proc, what))
                
                for i in range(0, proc):
                    min_limit = int(j + what * i)
                    max_limit = int(j + what * (i + 1))
                    
                    t = SQLiteTest()
                    t.start()
                    t.join()

                    end = time()
                    elapsed = end - start
                    j += e
                    print(j)
                    print("Time elapsed: %.5f\n" % elapsed)

        exit()

        # Escenario 3
        print("\nScenario 3:")
        
        for e in elements:
            for proc in process:
                start = time()
                what = e/proc
                
                print('ins = %d \t procs = %d \t per = %d'
                      % (e, proc, what))
                
                for i in range(0, proc):
                    p = Process(target=test.select_with_index,
                                args=(randint(1, e),))
                    p.start()
                    p.join()
                
                end = time()
                elapsed = end - start
                print("Time elapsed: %.5f\n" % elapsed)

        # Escenario 5
        print("\nScenario 5:")
        
        for e in elements:
            for proc in process:
                start = time()
                what = e/proc
                
                print('ins = %d \t procs = %d \t per = %d'
                      % (e, proc, what))
                
                for i in range(0, proc):
                    p = Process(target=test.select,
                                args=(randint(1, e),))
                    p.start()
                    p.join()
                
                end = time()
                elapsed = end - start
                print("Time elapsed: %.5f\n" % elapsed)
            
        
    except sqlite3.Error as e:
        print("DB error: {} s".format(e))
                    
    test.close()
