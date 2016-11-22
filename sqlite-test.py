from multiprocessing import Process
from time import time

import threading
import sqlite3
# import MySQLdb
import sys
import os

class SQLiteTest:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)          
        self.cursor = self.connection.cursor()
        self.lock = threading.Lock()

    def commit(self):
        self.connection.commit()
        
    def close(self):
        self.connection.close()

    def insert(self, min_limit, max_limit):
        '''Insert a number of elements into the table table'''
        try:
            self.lock.acquire(True)
            for i in range(min_limit, max_limit):
                cursor.execute('INSERT INTO test VALUES(?, ?, ?)',
                               (i, "ESTE ES EL TEXTO DE PRUEBA NUMERO " + \
                                str(i), i))
            self.connection.commit()
        finally:
            self.lock.release()

if __name__ == "__main__":
    test = SQLiteTest('sqlite-test.db')
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
        test.insert(0, 1000000)

    except sqlite3.Error as e:
        pass

    print("Success!\n")
    
    try:
        elements = [10, 1000, 100000, 300000]
        process = [1, 10, 50]
        j = 1000000 # Hardcoded, yes!
        
        # Escenario 1
        print("\nScenario 1:")
        
        for proc in process:
            for e in elements:
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
        if sys.argv[1] != "s":
            test.close()
            print("\nScenario 2")

            threads = list()
            for proc in process:
                for e in elements:
                    start = time()
                    what = e/proc
                    
                    print('ins = %d \t procs = %d \t per = %d'
                          % (e, proc, what))
                
                    for i in range(0, proc):
                        min_limit = int(j + what * i)
                        max_limit = int(j + what * (i + 1))
                    
                        t = threading.Thread(target=connect,
                                             args=(min_limit, max_limit))
                        threads.append(t)
                        t.start()
                    
                        end = time()
                        elapsed = end - start
                        j += e
                        print(j)
                        print("Time elapsed: %.5f\n" % elapsed)
        
    except sqlite3.Error as e:
        print("DB error: {} s".format(e))
                    
    test.close()
