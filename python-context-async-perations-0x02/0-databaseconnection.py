import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        # Open the database connection
        self.conn = sqlite3.connect(self.db_name)
        return self.conn  # This object is used as `conn` inside the `with` block

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Always close the connection
        if self.conn:
            self.conn.close()

# Use the custom context manager to run a query
if __name__ == "__main__":
    with DatabaseConnection("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        for user in users:
            print(user)
