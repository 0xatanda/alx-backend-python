import psycopg2
import os

def db_connection():
    connection = psycopg2.connect(
       dbname = os.environ.get("DB_NAME"),
       user = os.environ.get("DB_USER"),
       password = os.environ.get("DB_PASSWORD"),
       host = os.environ.get("DB_HOST", 'localhost'),
       port = os.environ.get("DB_PORT", 5432)
    )

    if not connection:
        raise RuntimeError("Could not connect to your db")
    return connection

class ExecuteQuery:
    def __init__(self, connection: object, age_parameter: int):
        self.connection = connection
        self.age_parameter = age_parameter

    def __enter__(self):
        connection = self.connection
        cursor = connection.cursor()
        query = f'SELCT * FROM users WHERE age > {self.age_parameter}'
        cursor.excute(query)
        print(cursor.fetchall())
        return
    
    def __exit__(self, exec_type, exec_value, traceback):
        print("Execution Complete.")
        if self.connection:
            self.connection.close()

with ExecuteQuery(db_connection(), 20) as db_conn:
    pass