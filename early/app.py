from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123", }
donations = []
authorized_user = ""

while True:
    show_homepage()
    if authorized_user == "":
        print("\nYou must be logged in to donate.")
        print()
    else:
        print(f"\nLogged in as {authorized_user}.")
        print()
    option = input("Choose an option:\t")
    if option == "1":
        username = input("Username:\t")
        password = input("Password:\t")
        authorized_user = login(database, username, password)
    elif option == "2":
        username = input("Please enter a username:\t")
        password = input("Please enter a password:\t")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
    elif option == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
    elif option == "4":
        show_donations(donations)
    elif option == "5":
        print("Leaving Donateme . . .")
        break
