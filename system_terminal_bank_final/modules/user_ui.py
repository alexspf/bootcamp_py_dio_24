from modules.user_model import UserData
from modules.utils import os
from modules.operations import *

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