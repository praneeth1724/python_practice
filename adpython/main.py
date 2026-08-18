import login
import MySQLdb as sql
db = sql.connect(
        host = "localhost",
        user = "root",
        passwd = "p172408",
        database = "LOGIN"
     )

cursor = db.cursor()
print("welcome to appname")
print("======================")
print("       appname     ")
print("======================")
print("1.Sign in 2.sign up")
val = int(input("enter 1 or 2:"))
if val == 1:
    login.signin(db,cursor)
elif val == 2:
    login.signup(db,cursor)
else:
    print("invalid input")
