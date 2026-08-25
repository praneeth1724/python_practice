import MySQLdb as sql
from MySQLdb import Error

database = sql.connect(
        host ="localhost",
        user ="root",
        password ="p172408",
        database ="LOGIN"
        )

cursor = database.cursor()
#creating table
tabc = """CREATE TABLE IF NOT EXISTS login_attempts(
          id INT AUTO_INCREMENT,
          username VARCHAR(50) NOT NULL,
          attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
          status VARCHAR(50) NOT NULL,
          PRIMARY KEY (id)
          );"""
cursor.execute(tabc)
database.commit()
def log_attempt(db, cursor, username, status):
    query = "INSERT INTO login_attempts (username, status) VALUES(%s, %s)"
    val = (username, status)

    try:
        cursor.execute(query, val)

        db.commit()
        print(f"successfully logged {status} attempt for user: {username}")

    except Error as e: 
        print(f"Database error occurred: {e}")

        try:
            db.rollback()
            print("transaction rolled back successfully.")
        except Error as rollback_err:
            print(f"Failed to rollback:{rollback_err}")


log_attempt(database, cursor, "user1", "success")
