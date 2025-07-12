import sqlite3

def setup_database():
    conn = sqlite3.connect('users.db') 
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    cursor.execute('SELECT COUNT(*) FROM users')
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            'INSERT INTO users (name, email) VALUES (?, ?)',
            [('Alice', 'alice@example.com'), ('Bob', 'bob@example.com')]
        )
    conn.commit()
    conn.close()

def main():
    setup_database()  
    print("Database is ready!")

if __name__ == "__main__":
    main()
