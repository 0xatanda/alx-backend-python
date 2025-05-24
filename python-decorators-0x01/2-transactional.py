import sqlite3
import functools

# Decorator to handle opening and closing the database connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try: 
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# Decorator to handle transaction management (commit or rollback)
def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(f"[ERROR] Transaction failed: {e}")
            raise
        return wrapper
    
@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email =?", (new_email, user_id))

#Update user's email with automatic transaction handling
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')