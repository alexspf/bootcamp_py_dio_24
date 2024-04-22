import os
class UserData:
    def __init__(self, name, statement, history):
        self.name: Any = name
        self.statement: Any = statement
        self.history: list = []

user = UserData('zeca', 1000, [])  ## is a simple bank, but implemention for user is here

def deposit() -> None:
    """"option to deposit"""
    value: int = get_option(1)
    user.statement += value
    user.history.append(f'{user.name} depositou {value}')
    return
def withdraw():
    """"option for withdraw"""
    while True:
        value: int = get_option(2)
        if value <= user.statement + 500:                ## fees :P
            break
        else:
            continue
    user.statement -= value
    user.history.append(f'{user.name} sacou {value}')
    return
def statement() -> str:
    """"option for statement"""
    return f'o seu saldo é {user.statement}'

def get_option(get) -> int:
    """"Print options and get option for user"""
    try:
        match get:
            case 0:    ## centralize string :p
                return int(input(f'==============================================================================\nOla bien viendo {user.name} to sistema bancaro do zecatatu\n==============================================================================\nEscolha zeca\n[1]Ver saldo\n[2]depositar\n[3]sacar\n[4]Historico de operações\n[5]Sair\n==========================\n           '))

            case 1:
                return int(input('Quanto deseja depositar?\n'))

            case 2:
                return int(input('Quanto deseja sacar?\n'))
            case 3:
                os.system('clear')
                for x in user.history:
                    print(f"==============================================================================\n{x}\n")
                input(f'pressione uma tecla para sair\n')
                return                       
                  
    except Exception:
        operation()
            
def operation() -> None:
    while True:
        get = 0
        option: int = get_option(get)
        match option:

            case 1:
                os.system('clear')
                print (statement())
            
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