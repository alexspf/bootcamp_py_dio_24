import os


class UserData:
    def __init__(self, name, statement, history):
        self.name = name
        self.statement = statement
        self.history = history


user = UserData('zeca', 1000, [])  # is a simple bank, but implementation for user is here


def deposit() -> None:
    """Option to deposit"""
    value = get_option(1)
    user.statement += value
    user.history.append(f'{user.name} depositou {value}')


def withdraw() -> None:
    """Option for withdraw"""
    value = get_option(2)
    if value > user.statement + 500:  # fees :P
        withdraw_erro()

    elif value == 0:
        operation()

    else:
        user.statement -= value
        user.history.append(f'{user.name} sacou {value}')

def withdraw_erro() -> None:
    os.system('clear')
    print('Saldo insuficiente para sacar esse valor, pressione um valor vazio para voltar ao menu')
    withdraw()

def statement() -> str:
    """Option for statement"""
    return f'O seu saldo é R${user.statement:.2f}'


def get_option(get) -> float:
    """Print options and get option for user"""
    try:
        match get:
            case 0:  # centralize string :p
                return float(input(f'''
==============================================================================
Ola bien viendo {user.name} to sistema bancaro do zecatatu
==============================================================================
Escolha zeca
[1]Ver saldo
[2]Depositar
[3]Sacar
[4]Historico de operações
[5]Sair
==========================
'''))

            case 1:
                return float(input('Quanto deseja depositar? R$'))

            case 2:
                return float(input('Quanto deseja sacar? R$'))

            case 3:
                os.system('clear')
                for x in user.history:
                    print(f"{x}\n")
                input('Pressione uma tecla para sair\n')
                return


    except Exception:
        operation()


def operation() -> None:
    while True:
        get = 0
        option = get_option(get)
        match option:
            case 1:
                os.system('clear')
                print(statement())

            case 2:
                deposit()
                os.system('clear')

            case 3:
                withdraw()
                os.system('clear')

            case 4:
                get_option(3)

            case 5:
                break
         


operation()
