import getpass
import os 
class UserData:
    def __init__(self, name: str, statement: float, history: list, password_crypt: str):
        self.name = name
        self.statement = statement
        self.history = history
        self.password_crypt = password_crypt



###operations

def operation(user: UserData, option : int,) -> None:
    match option:
  
            case 2:
                deposit(user)
                return True
                
            case 3:
                withdraw(user)
                return True
        
            case 4:
                return user.history

def deposit(user: UserData) -> None:
    """Option to deposit"""
    value = get_user_option(1, user)
    user.statement += value
    user.history.append(f'{user.name} deposited {value}')

def withdraw(user: UserData) -> None:
    """Option for withdraw"""
    value = get_user_option(2, user)
    if value > user.statement + 500:  # fees :P
        withdraw_error(user)

    elif value == 0:
        operation_ui(user)

    else:
        user.statement -= value
        user.history.append(f'{user.name} withdrew {value}')


def withdraw_error(user: UserData) -> None:
    clear()
    print('Insufficient balance to withdraw that amount. Please try again.')
    withdraw(user)

def statement(user: UserData) -> str:
    """Option for statement"""
    return f'Your balance is ${user.statement:.2f}'



##user interface
def get_user_option(option: int, user: UserData) -> int:
    """Print options and get option for user"""

    match option:
        case 0:  # centralize string :p
            return int(input(f'''
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

        
        case _:
            return get_user_option(0, user)

def operation_ui(user: UserData)   -> None:
    while True:
        option: int = get_user_option(0, user)
        match option:
            case 1:
                clear()
                print(statement(user))

            case 2:
                operation(user, 2)
                clear()

            case 3:
                operation(user, 3)
                clear()

            case 4:
                clear()
                
                print('Transaction History:')
                for x in operation(user, 4):
                    print(f"{x}\n")
                input('Press any key to exit\n')
                clear()
                
            case 5:
                print("Thank you for using the Zecatatu Bank System. Goodbye!")
                break

def clear() -> None:
    """Clear the console"""
    os.system('clear')

### login    

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


  

def start() -> None:
    user: UserData = login_or_create_user()

    operation_ui(user)

Data_base = UserData('alex', 10000, [], '1234')
start()
