import time
import sqlite3
import functools

# In-memory query cache dictionary
query_cache = {}

# Decorator to manage DB connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# Decorator to cache results based on query string
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        # Get the query from args or kwargs
        query = kwargs.get('query') or (args[0] if args else None)
        if query in query_cache:
            print("Returning cached result for query.")
            return query_cache[query]

        # Not cached, execute and store result
        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        print("🗃️ Caching result for query.")
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call: result is cached
users = fetch_users_with_cache(query="SELECT * FROM users")
print("Users:", users)

# Second call: result comes from cache
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print("Cached Users:", users_again)
