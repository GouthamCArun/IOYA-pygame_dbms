import random
import sqlite3



def PickTask(player_id):
    connection = sqlite3.connect("game_database.db")
    cursor = connection.cursor()
    random_number = random.randint(1, 4)
    
    cursor.execute("UPDATE Players SET TaskID=? WHERE PlayerID=?", (random_number, player_id))
    cursor.execute("UPDATE Players SET status='FALSE' WHERE PlayerID=?",(player_id,))
    connection.commit()
    print(f"your task id is {random_number}")
    return random_number
    connection.close()

