import os
import getpass


class UserData:
    def __init__(self, name, statement, history, password_crypt):
        self.name = name
        self.statement = statement
        self.history = history
        self.password_crypt = password_crypt


Data_base = UserData('alex', 10000, [],'1234')


def deposit(user) -> None:
    """Option to deposit"""
    value = get_option(1)
    user.statement += value
    user.history.append(f'{user.name} deposited {value}')


def withdraw(user) -> None:
    """Option for withdraw"""
    value = get_option(2)
    if value > user.statement + 500:  # fees :P
        withdraw_error()

    elif value == 0:
        operation(user)

    else:
        user.statement -= value
        user.history.append(f'{user.name} withdrew {value}')


def withdraw_error() -> None:
    os.system('clear')
    print('Insufficient balance to withdraw that amount, press any key to return to the menu')
    withdraw(user)


def statement(user) -> str:
    """Option for statement"""
    return f'Your balance is ${user.statement:.2f}'


def get_option(get) -> float:
    """Print options and get option for user"""
    try:
        match get:
            case 0:  # centralize string :p
                return float(input(f'''
==============================================================================
Hello {user.name}, welcome to the Zecatatu Bank System
==============================================================================
Choose an option:
[1] View balance
[2] Deposit
[3] Withdraw
[4] Transaction history
[5] Exit
==========================
'''))

            case 1:
                return float(input('How much do you want to deposit? $'))

            case 2:
                return float(input('How much do you want to withdraw? $'))

            case 3:
                os.system('clear')
                for x in user.history:
                    print(f"{x}\n")
                input('Press any key to exit\n')
                return

    except Exception:
        operation(user)


def operation(user) -> None:
    while True:
        get = 0
        option = get_option(get)
        match option:
            case 1:
                os.system('clear')
                print(statement(user))

            case 2:
                deposit(user)
                os.system('clear')

            case 3:
                withdraw(user)
                os.system('clear')

            case 4:
                get_option(3)

            case 5:
                break


def create_new_user() -> UserData:
    """Create a new user"""
    name = input("Enter the user's name: ")
    if name == Data_base.name:
        print("User already exists. Please try again.")
        return None
    statement = float(input("Enter the initial balance: "))
    password = getpass.getpass("Enter the password: ")
    history = []
    return UserData(name, statement, history, password)


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


if __name__ == "__main__":
    user = login_or_create_user()
    operation(user)
