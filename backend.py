import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("create table if not exists book(id integer PRIMARY KEY,title text,author text,year integer,ISBN integer)")
    conn.commit()
    conn.close()


def insert(title,author,year,ISBN):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("insert into book values(null,?,?,?,?)",(title,author,year,ISBN))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("select * from book")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("delete from book where id=?",(id,))
    conn.commit()
    conn.close()

def search(title="",author="",year="",ISBN=""):
     conn=sqlite3.connect("books.db")
     cur=conn.cursor()
     cur.execute("select * from book where title=? or author=? or year=? or ISBN=?",(title,author,year,ISBN))
     rows=cur.fetchall()
     conn.close()
     return rows

def update(id,title,author,year,ISBN):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("update book set title=?,author=?,year=?,ISBN=? where id=?",(title,author,year,ISBN,id))
    conn.commit()
    conn.close()

connect()




