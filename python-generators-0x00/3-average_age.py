import mysql.connector

def stream_user_ages():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # 🔁 Replace with your credentials
            password="Somi@2020",
            database="ALX_prodev"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")

        for row in cursor:
            yield row[0]  # Yield only the age (not the tuple)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def compute_average_age():
    total_age = 0
    count = 0

    for age in stream_user_ages():  # 1 loop
        total_age += age
        count += 1

    if count == 0:
        print("No users found.")
    else:
        average = total_age / count
        print(f"Average age of users: {average:.2f}")
