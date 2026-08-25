import MySQLdb as sql

db = sql.connect(
        host="localhost",
        user="root",
        password="p172408",
        database="NEW"
        )

cursor = db.cursor()
#creating table
tab = """CREATE TABLE IF NOT EXISTS accounts(
         username VARCHAR(50) UNIQUE,
         balance DECIMAL(10,2) NOT NULL
         );"""
cursor.execute(tab)
def transfer_funds(db, cursor, sender, receiver, amount):
    fecth = "SELECT balance FROM accounts WHERE username = %s;"
    cursor.execute(fecth, (sender,))
    senderbal = cursor.fetchone()
    f2 = "SELECT balance FROM accounts WHERE username = %s;"
    cursor.execute(f2, (receiver,))
    #recebal is receiver balance
    recebal = cursor.fetchone()
    #sbal is senderbalance, rbal is recevierbalance
    for sbal in senderbal:
        #sat is sender after balance
        sat = sbal - amount
    for rbal in recebal:
        #rat is receiver after balance
        rat = rbal + amount

    update = """UPDATE accounts
                SET balance = CASE
                    WHEN username = %s THEN %s
                    WHEN username = %s THEN %s
                    ELSE balance
                END
                WHERE username IN (%s, %s);"""
    data = (sender, sat, receiver, rat, sender, receiver)
    cursor.execute(update, data)
    db.commit()
    q1 = "SELECT balance FROM accounts WHERE username = %s"
    cursor.execute(q1, (sender,))
    sbat = cursor.fetchone()
    q2 = "SELECT balance FROM accounts WHERE username = %s"
    cursor.execute(q2, (receiver,))
    rbat = cursor.fetchone()
    for sfbal, rfbal in zip(sbat, rbat):
        print(f"after transfer sender {sender} balance is {sfbal} , receiver {receiver} balance is {rfbal}")



sender = input("enter senders name:")
receiver = input("enter receiver name:")
amount = int(input("enter amount to send:"))


transfer_funds(db, cursor, sender, receiver, amount)



