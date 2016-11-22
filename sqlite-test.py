from multiprocessing import Process
from time import time

import sqlite3
# import MySQLdb
import sys
import os

class SQLiteTest:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)          
        self.cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()
        
    def close(self):
        self.connection.close()
        

if __name__ == "__main__":
    test = SQLiteTest('sqlite-test')
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
        for i in range(0, 1000000):
            test.cursor.execute('INSERT INTO test VALUES(?, ?, ?)',
                                (i, "ESTE ES EL TEXTO DE PRUEBA NUMERO " + \
                                 str(i), i))
        test.commit()
    except sqlite3.Error as e:
        pass

    try:
        # Escenario 1
        elements = [10, 1000, 100000, 300000]
        process = [1, 10, 50]
        j = 1000001 # Hardcoded, yes!
        
        for p in process:
            for e in elements:
                what = p/e
                print('Now inserting %d new elements, using %d process. %d per process' % (e, p, what))
                cursor.execute('')
        
    except sqlite3.Error as e:
        print("DB error: {}".format(e))
                    
    test.close()
