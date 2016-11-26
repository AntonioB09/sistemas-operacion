import threading
import os
import sys
import sqlite3

class Test(threading.Thread):
    
    def __init__(self, lock):
        threading.Thread.__init__(self)
        self.text = "jodete"
        self.conn = sqlite3.connect('test.db')
        self.cursor = self.conn.cursor()
        self.lock = lock

    def execute(query):
        self.cursor.execute(query)

    def run(self):
        self.lock.acquire()
        print("%s:" % self.name)
        for i in range(100):
            self.cursor.execute(
                """
                INSERT INTO test VALUES(?, ?, ?)
                """, (i, i*i, 2*i))
        self.connection.commit()
        self.lock.release()
        

class FetchUrls(threading.Thread):
    """
    Thread cheking URLs.
    """
    def __init__(self, urls, output, lock):
        """
        Constructor
        @param urls list of urls
        @param output file to write urls output
        """
        threading.Thread.__init__(self)
        self.urls = urls
        self.output = output
        self.lock = lock
        
    def run(self):
        """
        Thread run method. Check URLS one by one
        """
        while self.urls:
            url = self.urls.pop()
            req = urllib.urlretrieve(url)
            try:
                d = urllib.urlopen(req)
            except urllib.URLError as e:
                print('URL %s failed: %s' % (url, e.reason))

            print('write done by %s' % self.name)
            print('URL %s fetched by %' % (url, self.name))
                
def main():
    urls1 = ['http://www.google.com', 'http://www.facebook.com']
    urls2 = ['http://www.yahoo.com', 'http://www.youtube.com']
    f = open('output.txt', 'w+')
    lock = threading.Lock()

    MAX_ELEMS = 1000
    lock = threading.Lock()
    test = Test(lock)
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
        

    except sqlite3.Error as e:
        pass

    print("Success!\n")

    t1 = Test()
    t2 = Test()
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # t1 = FetchUrls(urls1, f)
    # t2 = FetchUrls(urls2, f)
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # f.close()

if __name__ == '__main__':
    main()
