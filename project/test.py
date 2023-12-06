import sqlite3

def describe_table(table_name):
    # Connect to the SQLite database
    connection = sqlite3.connect("game_database.db")
    cursor = connection.cursor()

    # Execute the PRAGMA statement to get information about the table
    # cursor.execute(f"PRAGMA table_info({table_name})")

    # Insert a new record into the Users table
    # cursor.execute("INSERT INTO Users VALUES (101, 'Vasu', '1234', 'vasu@gmail.com', '12-12-2022', 0)")

    # Commit the changes
    connection.commit()

    # Fetch all the rows from the Users table
    cursor.execute("SELECT * FROM Users")
    rows = cursor.fetchall()

    # Print the column information
    print(f"Columns in the '{table_name}' table:")
    for row in rows:
        print(row)

    # Close the connection
    connection.close()

if __name__ == "__main__":
    # Replace "Users" with the actual table name you want to describe
    describe_table("Users")
