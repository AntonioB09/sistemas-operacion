from multiprocessing import Process
from time import time
from random import randint

import threading
import MySQLdb
import sys
import os

class MySQLTest:

    def __init__(self, database):
        self.connection = MySQLdb.connect(host="localhost",
                                          user="root",
                                          passwd="gh1290yu",
                                          db=database)      
        self.cursor = self.connection.cursor()
        self.lock = threading.Lock()

    def commit(self):
        self.connection.commit()
        
    def close(self):
        self.connection.close()

    def insert(self, min_limit, max_limit):
        '''Insert a number of elements into the table table'''
        for i in range(min_limit, max_limit):
            cursor.execute('INSERT INTO test VALUES(%d, "%s", %d)' % 
                           (i, "ESTE ES EL TEXTO DE PRUEBA NUMERO "+str(i), i))
        self.connection.commit()

            
    def select_with_index(self, index):
        '''Select a random record using indexes'''
        cursor.execute('SELECT * FROM test WHERE id=%d' % index)

    def select(self, pseudo_index):
        '''Select a random record using an not indexed id'''
        cursor.execute('SELECT * FROM test WHERE id2=%d' % pseudo_index)        

if __name__ == "__main__":
    test = MySQLTest('mysqltest')
    cursor = test.cursor
        
    # Create test table
    try:
        cursor.execute('CREATE TABLE test('
                       'id INT PRIMARY KEY AUTO_INCREMENT,'
                       'texto VARCHAR(255),'
                       'id2 INT)') # remember, 255 chars for MySQL
        print('CREATE TABLE')

        # Create index for the test table
        cursor.execute('CREATE INDEX id ON test (id)')
        print('CREATE INDEX')

        # Fill table with 1000000 elements
        print("Filling...")
        test.insert(0, 1000000)

        print("xd")
        
    except MySQLdb.Error as e:
        pass

    print("Success!\n")
    
    try:
        elements = [10, 1000, 100000, 300000]
        process = [1, 10, 50]
        j = 1000000 # Hardcoded, yes!
        
        # Escenario 1
        print("\nScenario 1:")
        
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
        # print("\nScenario 2")
        
        # threads = list()
        # for e in elements:
        #     for proc in process:
        #         start = time()
        #         what = e/proc
                
        #         print('ins = %d \t procs = %d \t per = %d'
        #               % (e, proc, what))
                
        #         for i in range(0, proc):
        #             min_limit = int(j + what * i)
        #             max_limit = int(j + what * (i + 1))
                    
        #             t = threading.Thread(target=test.insert,
        #                                  args=(min_limit, max_limit))
        #             threads.append(t)
        #             t.start()

        #             end = time()
        #             elapsed = end - start
        #             j += e
        #             print(j)
        #             print("Time elapsed: %.5f\n" % elapsed)
        # test.close()
        # exit()


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
            
        
    except MySQLdb.Error as e:
        print("DB error: {} s".format(e))
                    
    test.close()
