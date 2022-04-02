from colorama import init, Fore, Style
init(autoreset=True)


def show_homepage():
    print()
    print(Fore.CYAN + Style.BRIGHT + "       === DonateMe Homepage ===")
    print(Fore.CYAN + Style.BRIGHT +
          "------------------------------------------")
    print(Fore.CYAN + Style.BRIGHT +
          "| 1.  Login        | 2.  Register        |")
    print(Fore.CYAN + Style.BRIGHT +
          "------------------------------------------")
    print(Fore.CYAN + Style.BRIGHT +
          "| 3.  Donate       | 4.  Show Donations  |")
    print(Fore.CYAN + Style.BRIGHT +
          "------------------------------------------")
    print(Fore.CYAN + Style.BRIGHT +
          "|               5.  Exit                 |")
    print(Fore.CYAN + Style.BRIGHT +
          "------------------------------------------")
    print()


total = 0


def donate(username):
    while True:
        donation_amt = input(Fore.CYAN + Style.BRIGHT +
                             "Enter amount to donate:\t")
        if donation_amt.isnumeric() == False or int(donation_amt) <= 0:
            print(Fore.RED + Style.BRIGHT +
                  "Please enter a valid amount greater than zero.")
        else:
            donation_string = Fore.BLUE + Style.BRIGHT + \
                username + " donated $" + donation_amt
            print(Fore.GREEN + Style.BRIGHT + "Thank you for donating!")
            global total
            total += int(donation_amt)
            break
    return donation_string


def show_donations(donations):
    print(Fore.BLUE + Style.BRIGHT + "\n--- All Donations ---")
    if donations == []:
        print(Fore.RED + Style.BRIGHT + "Currently, there are no donations.")
    else:
        for donation in donations:
            print(donation)
        print(Fore.BLUE + Style.BRIGHT + f"Total: ${total}")
