from colorama import init, Fore, Style
init(autoreset=True)


def login(database, username, password):
    if username in database:
        if database[username] == password:
            print(Fore.GREEN + Style.BRIGHT + f"\nWelcome back {username}!\n")
            return username
        else:
            print(Fore.RED + Style.BRIGHT +
                  f"Incorrect password for {username}.\n")
            return ""
    else:
        print(Fore.RED + Style.BRIGHT + "User not found.  Please register.\n")
        return ""


def register(database, username, password):
    if len(username) > 10 or username[0].isalpha() == False:
        print(Fore.RED + Style.BRIGHT +
              "Username must be 10 characters or less and must start with a letter.  Please try again.")
        return ""
    for letter in username:
        if letter.isalpha() == False and letter.isnumeric() == False:
            print(Fore.RED + Style.BRIGHT +
                  "Username must only contain alphanumeric characters.  Please try again.")
            return ""
    if len(password) < 5:
        print(Fore.RED + Style.BRIGHT +
              "Password must be at least 5 characters.  Please try again.")
        return ""
    if username in database:
        print(Fore.RED + Style.BRIGHT + "Username already registered.")
        return ""
    else:
        print(Fore.GREEN + Style.BRIGHT +
              f"Username {username} has been registered.")
        return username
