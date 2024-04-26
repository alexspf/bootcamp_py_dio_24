try:
    from modules.user_model import UserData
    from modules.input import get_value

    def operation(user: UserData, option : int,) -> None:
        match option:
                case 2:
                    deposit(user)
                    return True
                case 3:
                    withdraw(user)
                    return True                
                case 4:
                    return history(user)

    def deposit(user: UserData) -> None:
        """Option to deposit"""
        value = get_value(1)
        user.statement += value
        user.history.append(f'{user.name} deposited {value}')

    def withdraw(user: UserData) -> None:
        """Option for withdraw"""
        value = get_value(2)
        if value > user.statement + 500:  # fees :P
            withdraw_error(user)

        else:
            user.statement -= value
            user.history.append(f'{user.name} withdrew {value}')

    def withdraw_error(user: UserData) -> None:                ### wrong place   
        print('Insufficient balance to withdraw that amount. Please try again.')
        withdraw(user)

    def statement(user: UserData) -> str:
        """Option for statement"""
        return f'Your balance is ${user.statement:.2f}'

    def history(user: UserData) -> None:
        return user.history
except Exception: 
    input("")