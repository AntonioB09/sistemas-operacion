from multiprocessing import Process
import time
import sqlite3
import sys
import os

class SQLiteTest:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.max_registers = 1000 # max number of registers

    def commit(self):
        self.connection.commit()
        
    def close(self):
        self.connection.close()
        

if __name__ == "__main__":
    test = SQLiteTest('sqlite-test.db')
    cursor = test.cursor
    table_name = ("test")
    
    # Create test table
    cursor.execute('CREATE TABLE test('
                   'id integer,'
                   'texto text,'
                   'id2 integer)') # remember, 255 chars for MySQL
    print('CREATE TABLE')

    # Create index for the test table
    cursor.execute('CREATE INDEX id ON test (id)')
    print('CREATE INDEX')

    start = time.time()
    for i in range(0, 10001000):
        test.cursor.execute('INSERT INTO test VALUES(?, ?, ?)',
                        (i, "ESTE ES EL TEXTO DE PRUEBA NUMERO " + str(i), i))
        print(i)
    test.commit()
    
    done = time.time()
    elapsed = done - start
    print(elapsed)

    test.close()
