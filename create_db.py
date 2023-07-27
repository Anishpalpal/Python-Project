import sqlite3
from venv import create
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS empolyee(EID INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Email text,Gender text,Contact text,DOB text,DOJ text,Password text,Usertype text,Address text,Salary text)")
    con.commit()


    cur.execute("CREATE TABLE IF NOT EXISTS supplier(Invoice INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Contact text,Description text)")
    con.commit()


    cur.execute("CREATE TABLE IF NOT EXISTS category(CID INTEGER PRIMARY KEY AUTOINCREMENT,Name text)")
    con.commit()


    cur.execute("CREATE TABLE IF NOT EXISTS product(PID INTEGER PRIMARY KEY AUTOINCREMENT,Category text,Supplier text,Name text,Price text,Quantity text,Status text)")
    con.commit()


create_db()