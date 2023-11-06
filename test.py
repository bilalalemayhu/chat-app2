import mysql.connector



conn = mysql.connector.connect(
    host="localhost",
    user="root",
)


cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXIST user")


