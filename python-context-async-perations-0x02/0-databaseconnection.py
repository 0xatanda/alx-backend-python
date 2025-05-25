import psycopg2
import os


class DaatabaseContextManager:
    def _init_(self, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT):
        self.db_name = DB_NAME
        self.db_user = DB_USER
        self.db_host = DB_HOST
        self.db_password = DB_PASSWORD
        self.db_port = DB_PORT
        self.connection = None

    def _enter_(self):
        self.connection = psycopg2.connect(
            dbname = self.db_name,
            user = self.db_user,
            password = self.db_password,
            host = self.db_host,
            port = self.db_port
        )

        if not self.connection:
            raise RuntimeError("Context Manager could not connect with your db.")
        
        cursor = self.connection.cursor()
        cursor.execute("SELECT vsersion(), current_database()")
        result = cursor.fetchone()
        print(result)
        return self.connection
    
    def __exit__(self, exec_type, exc_value, traceback):
        if self.connection:
            self.connection.close()
            print("Your connection was closed successfully")
            return
        
with DaatabaseContextManager(
    os.environ.get("DB_NAME"),
    os.environ.get("DB_USER"),
    os.environ.get("DB_PASSWORD"),
    os.environ.get("DB_HOST", 'localhost'),
    os.environ.get("DB_PORT", 5433)
) as db_conn:
    cursor = db_conn.cursor()
    cursor.execute("SLECT * FROM user_data WHERE user_id = '5d6c699b-c6e5-4f28-a795-a8dbd55b00ff'")
    print(cursor.fetchall())