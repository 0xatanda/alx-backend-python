import seed

def stream_users_in_batches(batch_size):
    """Yields users one by one from the DB, in batches."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) as total FROM user_data")
    total_rows = cursor.fetchone()['total']

    for offset in range(0, total_rows, batch_size):
        cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (batch_size, offset))
        batch = cursor.fetchall()
        for user in batch:
            yield user

    cursor.close()
    connection.close()


def batch_processing():
    """Processes users over age 25."""
    print("Processing users in batches...")
    for user in stream_users_in_batches(100):  # Fixed batch size
        if user['age'] > 25:
            print(user)
