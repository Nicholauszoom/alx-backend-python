import mysql.connector
from mysql.connector import errorcode
import csv
import uuid
from decimal import Decimal

DB_NAME = "ALX_prodev"
# 1. Connect to MySQL Server
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Somi@2020"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# 2. Create database if it does not exist
def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Database {DB_NAME} created or already exists")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

# 3. Connect to ALX_prodev database
def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Somi@2020", 
            database=DB_NAME
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# 4. Create user_data table if not exists
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(5, 2) NOT NULL,
                INDEX(user_id)
            )
        """)
        print("Table user_data created successfully")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Failed creating table: {err}")

# 5. Insert data into table
def insert_data(connection, filename):
    try:
        cursor = connection.cursor()
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = Decimal(row['age'])

                # Check if user already exists (based on email for example)
                cursor.execute("SELECT * FROM user_data WHERE email = %s", (email,))
                if cursor.fetchone():
                    continue  # Skip duplicate

                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, name, email, age))

        connection.commit()
        print("Data inserted successfully")
        cursor.close()
    except Exception as e:
        print(f"Error inserting data: {e}")
