import MySQLdb as sql

print("connecting to database server")
db = sql.connect(
        host = "localhost",
        user = "root",
        passwd = "p172408",
        database = "NEW"
     )
cursor = db.cursor()
     
"""users = "CREATE TABLE USERS (
               NAME VARCHAR(20) NOT NULL,
               PASS VARCHAR(20) NOT NULL
               )" """

data = "INSERT INTO USERS (NAME,PASS) VALUES (%s, %s);"
rd = [ 
      ("praneeth", "p172408"),
      ("user1", "1234")
      ]

cursor.executemany(data,rd)
db.commit()
db.close()
    
    

