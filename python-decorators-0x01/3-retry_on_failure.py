import time
import sqlite3
import functools

# Decortor to handle opening and clossing the db connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            return func(conn, *args, **kwargs)
        finally: 
            conn.close()
    return wrapper

# Decoration to retry db operation on failure
def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0 
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    print(f"[WARNING] Attempt {attempt} failed: {e}")
                    if attempt < retries:
                        print(f"[INFO] Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        print(f"[ERROR] All retry attempts failed.")
                        raise
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure
def fetch_users_with_retry(conn):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Attempt to fetch users with automatic retry on failure
users = fetch_users_with_retry()
print(users)