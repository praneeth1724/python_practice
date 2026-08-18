import MySQLdb as sql

database = sql.connect( 
              host = "localhost",
              user = "root",
              passwd = "p172408",
              database = "NEW"
            )
cursor = database.cursor()
create = """CREATE TABLE IF NOT EXISTS books (
            id INT NOT NULL,
            title varchar(50) NOT NULL,
            author varchar(50) NOT NULL,
            published_year INT NOT NULL,
            is_available BOOLEAN
            )"""
cursor.execute(create)
print("===================")
print(" Welcome to libary")
print("===================")
print("Select the following task by its number to use it \n 1.Add a new book \n 2.view all books \n 3.Search for a book by its author \n 4.Delete a book by its id")
task = int(input("enter:"))
if task == 1:
    i = int(input("enter book id:"))
    ti = input("enter book title:")
    auth = input("enter book author:")
    year = input("enter year when book was published:")
    ava = input("is this book available 1.TRUE 2.FALSE:")
    text = ava.upper()
    avail = 0
    if text == "FALSE":
             avail = 1


    add = "INSERT INTO books(id, title, author, published_year, is_available) VALUES (%s, %s, %s, %s, %s)"
    val = (i, ti, auth, year, avail)
    cursor.execute(add, val)
    print("book added succesfully")
elif task == 2:
    view = "SELECT * FROM books"
    cursor.execute(view)
    row = cursor.fetchall()
    icon = "true"
    for them in row:
        if them[4] == 0:
                icon = "true"
        elif them[4] == 1:
            icon = "false"

        print(f"id: {them[0]} title: {them[1]} author: {them[2]} year: {them[3]} avaliable: {icon}")
elif task == 3:
    autho = input("enter author name to find book:")
    search = "SELECT title FROM books where author = %s"
    cursor.execute(search, (autho,))
    res = cursor.fetchone()
    print(f"author: {autho} book: {res[0]}")
elif task == 4:
    num = int(input("enter book id to delete it:"))
    dele = "DELETE FROM books WHERE id = %s"
    cursor.execute(dele, (num,))
    print("book deleted successfully")
else:
    print("invalid option")
database.commit()
database.close()
