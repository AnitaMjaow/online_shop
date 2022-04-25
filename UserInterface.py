from OnlineShop import OnlineShop
import sys


class UserInterface:
    def loginMenu(self):
        e = OnlineShop()
        # Calls the function welcome
        welcome()
        while True:
            print_menu()
            user_choice = input("Ange val: ")
            if user_choice == "1":
                getUser()
            elif user_choice == "2":
                e.CreateNewUser(self)
            elif user_choice == "3":
                sys.exit()


def welcome():
    # Prints out a Welcome message
    print(" "*80)
    print("(づ￣ ³￣)づ  Välkommen till Online Shoppen YAY!")
    print(" "*80)
    print("Vad vill du göra idag?")
    print(" "*80)


def print_menu():
    # Menu for login and user roles

    print("\nMeny")
    print(" "*80)
    print("1. Logga in")
    print("2. Registrera ny användare")
    print("3. Avsluta")


def login():
    # Menu for login and user roles

    print("\nMeny")
    print(" "*80)
    print("1. Logga in")
    print("2. Registrera ny användare")
    print("3. Avsluta")


def getUser():
    print("\nLogga in")
    fname = input("Förnamn: ")
    lname = input("Efternamn: ")
    login(fname, lname)


u = UserInterface()
u.loginMenu()
u.CreateNewUser()