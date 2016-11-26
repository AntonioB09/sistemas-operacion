# Class SQLiteTest

import sqlite3
import threading

class SQLiteTest(threading.Thread):

    def __init__(self, database, lock):
        threading.Thread.__init__(self)
        self.connection = sqlite3.connect(database)          
        self.cursor = self.connection.cursor()
        self.lock = lock

    def commit(self):
        self.connection.commit()
        
    def close(self):
        self.connection.close()

    def insert(self, min_limit, max_limit):
        '''Insert a number of elements into the table table'''
        self.lock.acquire()
        print('lock acquired by %s' % self.name)
        for i in range(min_limit, max_limit):
            self.cursor.execute('INSERT INTO test VALUES(?, ?, ?)',
                           (i, "ESTE ES EL TEXTO DE PRUEBA NUMERO "+str(i), i))
        self.connection.commit()
        self.lock.release()
            
    def select_with_index(self, index):
        '''Select a random record using indexes'''
        self.cursor.execute('SELECT * FROM test WHERE id=?', (index,))

    def select(self, pseudo_index):
        '''Select a random record using an not indexed id'''
        self.cursor.execute('SELECT * FROM test WHERE id2=?', (pseudo_index,))     
