# # import sqlite3

# # # Connect to the SQLite database
# # connection = sqlite3.connect("game_database.db")
# # cursor = connection.cursor()

# # # cursor.execute("UPDATE Tasks SET NPCID=4 WHERE TaskID=4")

# # # cursor.execute("INSERT INTO Players VALUES(1,'VASU',300,600,0,'FALSE')")


# # # Commit the changes
# # connection.commit()
# # # cursor.execute("UPDATE Players SET status='FALSE' WHERE PlayerID=1")
# # # Select all data from the 'users' table
# # # cursor.execute("SELECT * FROM NPCs")
# # # cursor.execute("SELECT * FROM Tasks")
# # rows = cursor.fetchall()


# # # Print the results
# # for row in rows:
    
# #     print(row)

# # # Close the connection
# # connection.close()
import sqlite3

def update_assignments():
    # Connect to the SQLite database
    connection = sqlite3.connect("game_database.db")
    cursor = connection.cursor()

    # Update the descriptions for assignments 2, 3, and 4
    # update_data = [
    #     ('SUBMIT SS ASSIGNMENT TO CHITRA MISS',1, 1),
    #     # ('SUBMIT SS TUTORIAL TO ANISHA MISS', 2,3),
    #     # ('SUBMIT DBMS RECORD TO  MISS', 1,4)
    # ]

    # for data in update_data:
    #     cursor.execute('''
    #         UPDATE Tasks
    #         SET Description = ?, NPCID = ?
    #         WHERE TaskID = ?
    #     ''', data)

    # # Commit the changes
    # connection.commit()

    # Query and print the updated data
    cursor.execute('SELECT * FROM Players')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Close the connection
    connection.close()

if __name__ == "__main__":
    update_assignments()
# import sqlite3

# def update_npc_names():
#     # Connect to the SQLite database
#     connection = sqlite3.connect("game_database.db")
#     cursor = connection.cursor()

#     # Update the names in the NPCs table
#     update_data = [
#         ('anisha', 2),
#         ('veena', 3)
#     ]

#     for data in update_data:
#         cursor.execute('''
#             UPDATE NPCs
#             SET Name = ?
#             WHERE NPCID = ?
#         ''', data)

#     # Commit the changes
#     connection.commit()

#     # Query and print the updated data
#     cursor.execute('SELECT * FROM NPCs')
#     rows = cursor.fetchall()

#     print("Updated NPCs table:")
#     for row in rows:
#         print(row)

#     # Close the connection
#     connection.close()

# if __name__ == "__main__":
#     update_npc_names()
# import sqlite3

# def update_assignments():
#     # Connect to the SQLite database
#     connection = sqlite3.connect("game_database.db")
#     cursor = connection.cursor()

#     # Update the descriptions for assignments 2, 3, and 4 and modify the last column values
#     update_data = [
#         ('SUBMIT SS ASSIGNMENT TO ANISHA MISS', 2, 2),
#         ('SUBMIT SS TUTORIAL TO ANISHA MISS', 3, 1),
#         ('SUBMIT DBMS RECORD TO CHITRA MISS', 4, 1)
#     ]

#     for data in update_data:
#         cursor.execute('''
#             UPDATE Tasks
#             SET Description = ?, NPCID = ?
#             WHERE TaskID = ?
#         ''', data)

#     # Commit the changes
#     connection.commit()

#     # Query and print the updated data
#     cursor.execute('SELECT * FROM Tasks')
#     rows = cursor.fetchall()

#     print("Updated Tasks table:")
#     for row in rows:
#         print(row)

#     # Close the connection
#     connection.close()

# if __name__ == "__main__":
#     update_assignments()
