import time
import sqlite3
import functools

query_cache = {}

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('user.db')
        try:
            return func(conn, *args, **kwargs)
        finally: 
            conn.close()
    return wrapper

def cache_query(func):
    def wraper(conn, query, *args, **kwargs):
        if query in query_cache:
            print('[cache] Returned cached Result')
            return query_cache[query]
        result = func(conn, query, *args, **kwargs)
        query_cache[query] = result
        return result
    return wraper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall

# First call caches the result
users = fetch_users_with_cache("SLECT * FGROM user_data")

# Secnd call return returns cached result 
users_again = fetch_users_with_cache(query="SELECT * FROM user_data")