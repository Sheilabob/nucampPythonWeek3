def login(database, username, password):
    if username in database:
        if database[username] == password:
            print(f"\nWelcome back {username}!\n")
            return username
        else:
            print(f"Incorrect password for {username}.\n")
            return ""
    else:
        print("User not found.  Please register.\n")
        return ""


def register(database, username):
    if username in database:
        print("Username already registered.")
        return ""
    else:
        print(f"Username {username} has been registered.")
        return username
