import sqlite3

class DataBase():
    def __init__(self, db):
         sqlite3.conn = sqlite3.connect(db)
         self.cur = self.conn.cursor()
         self.cur.execute("CREAT TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year TEXT, isbn TEXT)")
         self.conn.commit()

    def fetch(self):
         self.cur.execute("SELECT * FROM books")
         rows = self.cur.fetchall()
         return rows
    
    def insert(self, title, author, year, isbn):
         self.cur.execute("INSERT INTO books VALUES (NULL, ?, ?,? )" , (title, author, year, isbn))
         self.conn.commit()


    def remove(self, id):
         self.cur.execute("DELETE FROM books WHERE id = ?" , (id,))
         self.conn.commit()

    def update(self, id, title, author, year, isbn):
         self.cur.execute("UPDATE books SET title = ? , author = ?, year = ? , isbn = ? WHERE id = ?" , (title, author, year, isbn, id))
         self.conn.commit()
         
    def search(self, title, author, year, isbn):
         self.cur.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ?")
         rows = self.cur.fetchall()
         return rows
    
         
         
          





