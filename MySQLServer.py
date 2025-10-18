import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL server (adjust credentials as needed)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ponagalo@99"
    )

    cursor = conn.cursor()

    # Create database if it doesn't exist
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err}")

    # Close cursor and connection
    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")
