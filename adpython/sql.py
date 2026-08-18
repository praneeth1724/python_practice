import MySQLdb as sql
import hashlib

db = sql.connect(
        host = "localhost",
        user = "root",
        passwd = "p172408",
        database = "NEW"
     )
cursor = db.cursor()
     
def signup():
    usern = input("enter your name:")
    passw = input("enter your password:")
    #to hash the password
    hashed = hashlib.sha256().update(passw.encode('utf-8'))
    #to create database
    db = "CREATE DATABASE IF NOT EXISTS LOGIN;"
    #to create table
    table = "CREATE TABLE IF NOT EXISTS USERS(
                 id INTEGER PRIMARY KEY AUTOCT_ID AUTOINCREMENT,
                 username VARCHAR(40) UNIQUE NOT NULL,
                 password_hash CHAR(64) NOT NULL
                 )"
    cursor.execute(db)
    cursor.execute(table)
    #to insert user and his password
    try:
        cursor.execute("INSERT INTO USERS (username, password_hash) VALUES (?, ?)", (usern, hashed)
          )
        print(f"user '{usern}' signup success")
    except sql.IntegrityError:
        print("Username already exists try again")
def signin():
    usern = input("enter your name:")
    passw = input("enter your password:")
    hashed = hashlib.sha256().update(passw.encode('utf-8'))
    
    cursor.execute("SELECT password_hash FROM USERS WHERE username = ?", (usern))
    row = cursor.fetchone()
    if not row:
        print("user dosnt exist")
        return False
    if hashed == row:
        print("login success")
    else:
        print("incorrect password")
