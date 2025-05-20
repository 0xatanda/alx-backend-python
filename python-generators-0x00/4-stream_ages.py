import seed

def stream_user_ages():
    """Generator to stream user ages one at a time"""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield float(row[0])
    cursor.close()
    connection.close()

def compute_average_age():
    """Compute average age using streaming generator"""
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    if count > 0:
        average_age = total_age / count
        print(f"Average age of users: {average_age}")
    else:
        print("No users found.")

if __name__ == "__main__":
    compute_average_age()
