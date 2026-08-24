import MySQLdb as sql

database = sql.connect(
        host = "localhost",
        user = "root",
        password = "p172408",
        database = "shop"
        )

cursor = database.cursor()
#creating database
dbc = "CREATE DATABASE IF NOT EXISTS shop"
cursor.execute(dbc)
#creating table
tabc = """CREATE TABLE IF NOT EXISTS warehouse_stock(
         item_id INT UNIQUE,
         item_name VARCHAR(50) NOT NULL,
         quantity INT NOT NULL
         )"""
cursor.execute(tabc)
database.commit()
def check_reorder_status(cursor):
    query = "select * FROM warehouse_stock WHERE quantity < 10"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

less = check_reorder_status(cursor)
print(f"alert the following items are less in qunatity")
for item in less:
    print(item)



