import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='jam2003eft',
        database='nordicharvest'
    )
    if connection.is_connected():
        print("Connected to MySQL database")
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You're connected to the database:", record)

except Error as e:
    print(f"Error while connecting to MySQL: {e}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

if __name__ == '__main__':
    pass