from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register
from colorama import init, Fore, Style
init(autoreset=True)

database = {"admin": "password123"}
donations = []
authorized_user = ""
total = 0

while True:
    show_homepage()
    if authorized_user == "":
        print(Fore.RED + Style.BRIGHT + "You must be logged in to donate.\n")
    else:
        print(Fore.GREEN + Style.BRIGHT + f"Logged in as: {authorized_user}\n")

    option = input(Fore.CYAN + Style.BRIGHT + "Choose an option:\t")
    if option == "1":
        username = input(Fore.CYAN + Style.BRIGHT + "Username:\t").lower()
        password = input(Fore.CYAN + Style.BRIGHT + "Password:\t")
        authorized_user = login(database, username, password)
    elif option == "2":
        username = input(Fore.CYAN + Style.BRIGHT +
                         "Please enter a username:\t").lower()
        password = input(Fore.CYAN + Style.BRIGHT +
                         "Please enter a password:\t")
        authorized_user = register(database, username, password)
        if authorized_user != "":
            database[username] = password
    elif option == "3":
        if authorized_user == "":
            print(Fore.RED + Style.BRIGHT + "You are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
    elif option == "4":
        show_donations(donations)
    elif option == "5":
        print(Fore.MAGENTA + Style.BRIGHT + "Leaving DonateMe . . .")
        break
    else:
        print(Fore.RED + Style.BRIGHT + "Invalid entry. Please try afain.")
