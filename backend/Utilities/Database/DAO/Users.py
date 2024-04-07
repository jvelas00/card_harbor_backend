from Utilities.Database.DatabaseConnector import ConnectToDatabase

def GetUser(username, password):
    cur = ConnectToDatabase()

    cur.execute(
        "SELECT * FROM USERS WHERE username = ? AND password = ?",
        (username,password,))

    return cur.fetchall() 