from modules.user_model import UserData
from modules.user_model import Data_base
import getpass
def create_new_user() -> UserData:
    """Create a new user"""
    name = input("Enter the user's name: ")
    if name == Data_base.name:
        print("User already exists. Please try again.")
        return None
    try:
        statement = float(input("Enter the initial balance: "))
    except Exception:
        print("Invalid balance. Please try again.")
        return None 
    password = getpass.getpass("Enter the password: ")
    return UserData(name, statement, [], password)


def login_or_create_user() -> UserData:
    """Login or create a new user"""
    while True:
        choice = input("Do you want to login or create a new user? (login/create): ")
        if choice.lower() == "login":
            return user_login()
        elif choice.lower() == "create":
            user = create_new_user()
            if user is not None:
                return user
        elif choice == "0":
            return create_new_user()
        else:
            print("Invalid choice. Please try again.")


def user_login() -> UserData:
    """Login with existing user"""
    while True:
        name = input("Enter the user's name: ")
        if name != Data_base.name:
            print("User not found. Please try again.")
            continue
        password = getpass.getpass("Enter the password: ")
        if password == Data_base.password_crypt:
            return UserData(
                name,
                Data_base.statement,
                Data_base.history,
                Data_base.password_crypt,
            )
        else:
            print("Invalid password. Please try again.")