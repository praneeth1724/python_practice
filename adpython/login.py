import MySQLdb as sql
import hashlib

db = sql.connect(
        host = "localhost",
        user = "root",
        passwd = "p172408",
        database = "NEW"
     )
cursor = db.cursor()
     
def signup(db,cursor):
    usern = input("enter your name:")
    passw = input("enter your password:")
    #to hash the password
    hasher = hashlib.sha256()
    hasher.update(passw.encode('utf-8'))
    hash_pass = hasher.hexdigest()
    #to create database
    db1 = "CREATE DATABASE IF NOT EXISTS LOGIN;"
    #to create table
    table = """CREATE TABLE IF NOT EXISTS USERS(
                 id INT NOT NULL AUTO_INCREMENT,
                 username varchar(40) UNIQUE NOT NULL,
                 password_hash CHAR(64) NOT NULL,
                 PRIMARY KEY (id)
                 )"""
    """cursor.execute(db)"""
    cursor.execute(table)
    db.commit()
    #to insert user and his password
    try:
        cursor.execute("INSERT INTO USERS (username, password_hash) VALUES (%s, %s)", (usern, hash_pass)
          )
        db.commit()
        print(f"user '{usern}' signup success")
    except sql.IntegrityError:
        print("Username already exists try again")
def signin(db,cursor):
    usern = input("enter your name:")
    passw = input("enter your password:")
    hasher = hashlib.sha256()
    hasher.update(passw.encode('utf-8'))
    hash_pass = hasher.hexdigest()
    
    cursor.execute("SELECT password_hash FROM USERS WHERE username = %s", (usern,))
    row = cursor.fetchone()
    if not row:
        print("user dosnt exist")
        return False
    strhash = row[0]
    if hash_pass == strhash:
        print("login success")
    else:
        print("incorrect password")
